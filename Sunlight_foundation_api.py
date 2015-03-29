
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 16:57:43 2015

@author: prabhath
"""

import requests
import json

query_params = { 'apikey': 'get_the_from_site',
                'per_page': 3,
                'phrase': 'congratulations to you!',
                'sort': 'date desc'
                }		       
endpoint = 'http://capitolwords.org/api/text.json'

response = requests.get( endpoint, params=query_params)
response.text

data = json.loads(response.text)
print json.dumps(data)
