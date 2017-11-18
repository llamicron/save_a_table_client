import json
import os
import time
import requests
import RPi.GPIO as GPIO

path = os.path.dirname(os.path.abspath(__file__))

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)
GPIO.setup(5, GPIO.IN)
GPIO.setup(22, GPIO.OUT)

old_button_status = GPIO.input(5)


# url = 'http://ec2-54-200-137-241.us-west-2.compute.amazonaws.com:5000/update-table'
url = 'http://192.168.0.59:5000/update-table'


table = json.loads(open(path + "/table_data", 'r').read())

switch_state = 1

data = {
    'table': {
        'number': table['number'],
        'floor': table['floor'],
        'state': switch_state # Get this from the switch
    }
}

# Post data to save_a_table site
def post_data(url, data):
    request = requests.post(url, headers={'Content-Type': 'application/json'},  data=json.dumps(data))
    return request.text

# Log response in logfile
def log_response(response, posted_data):
    with open(path + "/table_log", 'a') as file:
        file.write("Request made at " + time.strftime("%H:%M:%S") + " on " + time.strftime("%d/%m/%Y") )
        file.write("\n")
        file.write("posted_data: ")
        file.write(str(data))
        file.write("\n")
        file.write("Response: " + response)
        file.write("\n")
        file.write("\n")

def write_log_failure(err):
    with open(path + "/table_log", 'a') as file:
        file.write("FAILURE: Failed request made at " + time.strftime("%H:%M:%S") + " on " + time.strftime("%d/%m/%Y"))
        file.write("\n")
        file.write("Is the server down? I think it's probably down... check it out. If you're not Luke, call Luke.\n")
        file.write("--- Exception ---\n")
        file.write(str(err))
        file.write("\n")
        file.write("\n")

# Detect switch loop, post data when flipped
while True:
    button_status = GPIO.input(5)
    if old_button_status != button_status:
        data['table']['state'] = button_status
        try:
            response = post_data(url, data)
            log_response(response, data)
        except requests.exceptions.ConnectionError as err:
            write_log_failure(err)
        old_button_status = button_status
    time.sleep(0.2)
GPIO.cleanup()
