
'''
Powerbot demo signals script
(c) 2018 Inercomp GmbH
'''

from powerbot import Configuration, ApiClient
from powerbot.api import SignalsApi
import os, logging
import json
import random
from datetime import datetime,timedelta

## Setting up logging and defining global variables
logging.basicConfig(level=logging.INFO)
LOGGER = logging.getLogger()

# Retrieving handles to the powerbot api
client = ApiClient()
client.set_default_header("api_key",os.environ['POWERBOT_PLAYGROUND_API_KEY'])

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
