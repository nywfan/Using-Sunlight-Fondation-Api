# Using-Sunlight-Api

An API is a set of  programming instructions and standards for accessing web
based software applications. A wrapper is an API client, that are commonly used
to wrap the API into easy to use functions by doing the API calls itself.

This a step by step intoduction for using Sunlight Foundation api using Python.

In order to make this work You need Api key provided by the Sunlight Foundation. Go through this link for the registration process http://sunlightfoundation.com/api/accounts/register/ as soon as you register you will get your own Api key.

# Modules needed to work with json and open url
1. requests
2. json
3. pprint
4. urllib2

If you do not have then they can be installed using the following command.
pip install "module_name"
Do not use the quotations. 

# Three steps for using 

* Once you know which URL you need to open and have imported the necessary modules,
we can use the request module to get the JSON feed.

```python
endpoint = 'http://capitolwords.org/api/text.json'
response = requests.get(endpoint)
response.text
```
* Once you done with getting the feed from the desired site. You need to convert the feed into dictionary.

```python
# Converting feed into dictionary
data = json.loads(response.text)
# The data is serialized using the json.dumps() method.
print json.dumps(data["results"][0])
```

* Now we have a python dictionary and we can start using it to get the results
we want.
A common way of doing that is to loop through the result and get the data that
you are interested in.

This can also be done using the query parameters the are specified along with the website's url. The parameters that can be given are specified in the Api document http://sunlightlabs.github.io/Capitol-Words/.

```python
query_params = { 'apikey': '148ea5f5075c4b54b0e55bfa0d59bce1',
                'per_page': 3,
                'phrase': 'congratulations to you!',
                'sort': 'date desc'
                }		       
endpoint = 'http://capitolwords.org/api/text.json'

response = requests.get( endpoint, params=query_params)
```


