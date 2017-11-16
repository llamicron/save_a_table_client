import requests
import json
import time
from os.path import expanduser

table_data_file = expanduser("~") + "/table_data"

url = 'http://ec2-54-200-137-241.us-west-2.compute.amazonaws.com:5000/update-table'

table = json.loads(open(table_data_file, 'r').read())

switch_state = 1

data = {
    'table': {
        'number': table['number'],
        'floor': table['floor'],
        'state': switch_state # Get this from the switch
    }
}

def post_data(url, data):
    request = requests.post(url, headers={'Content-Type': 'application/json'},  data=json.dumps(data))
    return request.text

def log_response(response, posted_data):
    with open(expanduser("~") + "/table_log", 'a') as file:
        file.write("Request made at " + time.strftime("%H:%M:%S") + " on " + time.strftime("%d/%m/%Y") )
        file.write("\n")
        file.write("posted_data: ")
        file.write(str(data))
        file.write("\n")
        file.write("Response: " + response)
        file.write("\n")
        file.write("\n")


response = post_data(url, data)
log_response(response, data)
