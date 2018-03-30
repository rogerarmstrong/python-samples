'''
Powerbot helper functions
(c) 2018 Inercomp GmbH
'''

from powerbot import Configuration, ApiClient
from powerbot.api import MarketApi,  OrdersApi, LogsApi
from powerbot.models import OrderEntry, OrderModify
import os, logging
import json
from datetime import datetime


def get_signal_value(contract, source, signal_name):
    '''
    Retrieves the signals from the contract
    '''    
    if contract and contract.signals:
        for s in contract.signals:
            if s.source == source and signal_name in s.value:
                return s.value[signal_name]

    return None

def get_previous_values(order):
    '''
    Helper function to retrieve values from the previous iteration
    '''
    order_type = None
    prev_hour_counter = None
    prev_marginal_price = None
    if order and order.txt:
        try:
            data = json.loads(order.txt)
            order_type = data['type']
            prev_hour_counter = data['hour_counter']
            prev_marginal_price = data['marginal_price']
        except:
            pass
    return order_type, prev_hour_counter, prev_marginal_price
