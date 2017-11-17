"""
Don't use this script, use the other one
"""
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(5, GPIO.IN)
GPIO.setup(22, GPIO.OUT)

old_button_status = GPIO.input(5)

while True:
    button_status = GPIO.input(5)
    # Don't know if this is necessary...
    # GPIO.output(22, button_status)
    if old_button_status != button_status:
        # Here it is
        print(button_status)
        old_button_status = button_status
    time.sleep(0.2)
GPIO.cleanup()
