
import requests
import json
import jsonpath


# API URL
url = 'https://reqres.in/api/users?page=2'

resp = requests.get(url)


# Parse Response to JSON format

json_resp = json.loads(resp.text)
# print json_resp

# Fetch Value using JSON Path

pages = jsonpath.jsonpath(json_resp,'total_pages')


try:
    assert pages[0] == 5
except:
    print 'pages value not matching'