
import requests
import json
import jsonpath

url = 'https://reqres.in/api/users'

# Read Inpput JSON File

file = open('C:\\Biswadip\\APIAutomation\\CreateUser.json', 'r')
json_input = file.read()

req_json = json.loads(json_input)

# Make POST Request with JSON Input Body

resp = requests.post(url, req_json)

print resp.content

try:
    assert (resp.status_code == 201)
except:
    print "Not Successgul POST Request"



# Fecth Header from Response

print resp.headers.get('Date')

# Parse Response to JSON Format

resp_json = json.loads(resp.text)

# PIck ID using JSONPATH

id = jsonpath.jsonpath(resp_json, 'id')

print id[0]

