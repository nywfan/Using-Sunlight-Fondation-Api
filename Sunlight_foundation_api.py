
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 16:57:43 2015

@author: prabhath
"""

import requests
import json

query_params = { 'apikey': '148ea5f5075c4b54b0e55bfa0d59bce1',
                'per_page': 3,
                'phrase': 'congratulations to you!',
                'sort': 'date desc'
                }		       
endpoint = 'http://capitolwords.org/api/text.json'

response = requests.get( endpoint, params=query_params)
response.text

data = json.loads(response.text)
print json.dumps(data)
