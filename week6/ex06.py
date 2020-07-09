import pprint

import requests

pp = pprint.PrettyPrinter(indent=4, depth=2)
# Making a GET request
x = requests.get('https://github.com/timeline.json')

# check status code for response received
# success code - 200
pp.pprint(x.content)
# pp.pprint(x.text)
# pp.pprint(x.json)
# pp.pprint(x.headers)

response = requests.post('https://httpbin.org/post', json={'id': 1, 'name': 'Jack'})
print("Status code: ", response.status_code)
print("Printing Entire Post Request")
pp.pprint(response.json())

newHeaders = {'Content-type': 'application/json', 'Accept': 'text/plain'}

response = requests.post('https://httpbin.org/post',
                         data={'id': 1, 'name': 'Jack'},
                         headers=newHeaders)

print("Status code: ", response.status_code)

response_Json = response.json()
print("Printing Post JSON data")
print(response_Json['data'])

print("Content-Type is ", response_Json['headers']['Content-Type'])
