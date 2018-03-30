
'''
Powerbot demo signals script
(c) 2018 Inercomp GmbH
'''

import os, logging, sys, json, random
from datetime import datetime,timedelta
from powerbot import Configuration, ApiClient
from powerbot.api import SignalsApi

## Setting up logging and defining global variables
logging.basicConfig(level=logging.INFO)
LOGGER = logging.getLogger()

#Demo script accepts api_key as commandline parameter or as an environmental variable
api_key = str(sys.argv[1]) if  len(sys.argv) == 2 else os.getenv('POWERBOT_PLAYGROUND_API_KEY')
if not api_key:
    raise ValueError("Please provide your api_key on the command line or as the 'POWERBOT_PLAYGROUND_API_KEY' environmen variable")

# Retrieving handles to the powerbot api
client = ApiClient()
client.set_default_header("api_key",api_key)

signals = SignalsApi(client)

hour = 0
now = datetime.utcnow()
while hour <= 24:
    hour+=1
    
    # Submit a demo ETRMSystem signal with a random imbalance between -10 and +10 MW
    delivery_start = now.replace(minute=0, second=0, microsecond=0) + timedelta(hours=hour)
    signals.update_signal(
        id=delivery_start.strftime("etrm_signal_%Y-%m-%dT%H"),
        source = "ETRMSystem",
        value = {
            "imbalance": round(random.uniform(-10,10),2),
            "delivery_start" : delivery_start.strftime("%Y-%m-%dT%H:%M:%SZ"),
            "delivery_end" : (delivery_start + timedelta(hours=1)).strftime("%Y-%m-%dT%H:%M:%SZ")
        }
    )

    # Submit a demo OptSystem signal with a random marginal_price between 40 and 50
    signals.update_signal(
        id=delivery_start.strftime("opt_signal_%Y-%m-%dT%H"),
        source = "OptSystem",
        value = {
            "marginal_price": round(random.uniform(40,50),2),
            "delivery_start" : delivery_start.strftime("%Y-%m-%dT%H:%M:%SZ"),
            "delivery_end" : (delivery_start + timedelta(hours=1)).strftime("%Y-%m-%dT%H:%M:%SZ")
        }
    )
    


LOGGER.info("Signals completed.")
