'''
Powerbot demo algo script
(c) 2018 Inercomp GmbH
'''
import os, logging,sys,json
from datetime import datetime
# Powerbot api generated automatically from the open-api sepecification using
# https://swagger.io/swagger-codegen/
from powerbot import Configuration, ApiClient
from powerbot.api import MarketApi,  OrdersApi, LogsApi
from powerbot.models import OrderEntry, OrderModify
from algo_helper import get_previous_values, get_signal_value

## Setting up logging and defining global variables
logging.basicConfig(level=logging.INFO)
LOGGER = logging.getLogger()
PRODUCT = "Intraday_Power_D"

#Demo script accepts api_key as commandline parameter or as an environmental variable
api_key = str(sys.argv[1]) if  len(sys.argv) == 2 else os.getenv('POWERBOT_PLAYGROUND_API_KEY')
if not api_key:
    raise ValueError("Please provide your api_key on the command line or as the 'POWERBOT_PLAYGROUND_API_KEY' environmen variable")
    
# Retrieving handles to the powerbot api
client = ApiClient()
client.set_default_header("api_key",api_key)

market = MarketApi(client)
orders = OrdersApi(client)
logs = LogsApi(client)

if __name__ == '__main__':
    
    market_status = market.get_status()   
    if market_status.status == "OK":
        #Market is ok, start trading

        #Trading window -> the upcoming 6 hourly products
        order_book = orders.get_order_book(product=PRODUCT, limit=6) 
        hour_counter = 0 
        for contract in order_book.contracts:
            hour_counter+=1
            imbalance = get_signal_value(contract,"ETRMSystem","imbalance")
            marginal_price = get_signal_value(contract,"OptSystem","marginal_price")

            marginal_price_changed = False
            
            prev_hour_counter = None
            prev_marginal_price = None

            if imbalance and marginal_price:
                to_be_deleted = []
                own_orders = orders.get_own_orders(contract_id=contract.contract_id, offset=0, limit=20)
                current_quantity = 0
                for o in own_orders:
                    order_type, prev_hour_counter, prev_marginal_price = get_previous_values(o)
                    if order_type == "demo":
                        if o.buy:
                            current_quantity += o.quantity
                        else:
                            current_quantity -= o.quantity
                        to_be_deleted.append(o)    

                marginal_price_changed = True if prev_marginal_price and prev_marginal_price != marginal_price else False

                #TODO: Vorzeichenfehler bzw. absolutwert nehmen?  Derzeit ist (current_quantity + contract.relative_position != imbalance) IMMER false...
                if (current_quantity + contract.relative_position != imbalance) or marginal_price_changed: 
                   
                    # Delete previously placed orders
                    for o in to_be_deleted:
                        orders.modify_order(order_id=o.order_id,modifications=OrderModify(action="DELE"))

                    # Prepare new order
                    new_order = OrderEntry(prod=PRODUCT, 
                        contract_id = contract.contract_id, 
                        clearing_acct_type = "P",
                        ordr_exe_restriction = "NON",
                        type = "O",
                        validity_res = "GFS",
                        state = "ACTI",
                        quantity = 0,
                        price = 0)
                    
                    # Calculate quantity and price
                    delta_q = imbalance + contract.relative_position
                    quantity = 0
                    pricePremium = 0
                    if delta_q < 0:
                        new_order.side = "BUY"
                        quantity = abs(delta_q)
                        price_premium = - (hour_counter * 2 - 2) #TODO prev_hour_counter (eventually) holds the value from the last iteration, how should this influence the price at this point?
                    elif delta_q > 0:
                        new_order.side = "SELL"
                        quantity= delta_q
                        price_premium = hour_counter * 2 - 2

                    # Place new order
                    if quantity > 0:
                        #EPEX requires rounding to to 0.1 MW
                        new_order.quantity = round(quantity, 1) 
                        #Epex requires rounding to EUR 0.1
                        new_order.price = round(marginal_price + price_premium, 1) 
                        # Remember current values (for eventual next iteration)
                        new_order.txt = json.dumps({"type":"demo", "hour_counter": hour_counter, "marginal_price" : marginal_price})
                        orders.add_order(new_order)
                        LOGGER.info("Created {} order for {} for {} MW and price {}".format(new_order.side, contract.name, new_order.quantity, new_order.price))
                else:
                    LOGGER.info("Orders are already placed for contract {}. No changes since last iteration.".format(contract_name))
            else:
                LOGGER.info("No signals for contract {}".format(contract.name))        

        LOGGER.info("Algo finished.")

    else:
        LOGGER.error("Market not ready. {}".format(market_status))    

    # Fetch the logs generated by the EPEX Powerspot since the last run
    if os.path.exists('algo.json'):
        last_run = json.load(open('algo.json'))
    else:
        last_run = {"log_timestamp" : datetime.utcnow()}

    more_logs = True
    count = 0
    offset = 0
    while more_logs:
        # Fetch next 50 logs, iterate as long as nothing is received.
        count+=1
        if count > 100:
            LOGGER.info("More logs would be available, however.. aborting at this point.")
            break
        log_entries = logs.get_logs(offset=offset, limit=50, severity_at_least="MED",received_from=last_run['log_timestamp'])
        offset+=50
        more_logs = len(log_entries) > 0
        for l in log_entries:
            LOGGER.info("{},{}, {}".format(l.received,l.severity,l.text))
 
    # Remember the last log_timestamp in the "algo.json" file
    with open('algo.json', 'w') as f:
        json.dump({"log_timestamp" : datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")},f)



