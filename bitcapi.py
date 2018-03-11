# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 03:47:38 2018

@author: Anish
"""

import requests as req
import time

now =time.ctime()

bit = req.get('https://api.coindesk.com/v1/bpi/currentprice.json')
jsonbit = bit.json()['bpi']['USD']['rate']

print("1 Bitcoin is worth $" + jsonbit + " as of " + now)