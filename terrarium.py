################################################
############# TERRARIUM CODE ###################
################################################

# MOISTURE SENSOR CODE
from classes import Hardware
from classes import TimeKeeper as TK
import RPi.GPIO as GPIO
import time
 
#SENSOR SETUP
wschannel = 13
GPIO.setmode(GPIO.BCM)
GPIO.setup(wschannel, GPIO.IN)

#PUMP SETUP
SECONDS_TO_WATER = 10
RELAY = Hardware.Relay(12, False)
 
def waterpoll(wschannel):
        if GPIO.input(wschannel):
                print("Your plants have plenty of fresh water!")
                return True
        else:
                print("Your plants are dry!")
                return False

# DA PUMP CODE


def water_plant(relay, seconds):
    relay.on()
    print("Plant is being watered!")
    time.sleep(seconds)
    print("Watering is finished!")
    relay.off()

def main():
    test = 1
    #time_keeper = TK.TimeKeeper(TK.TimeKeeper.get_current_time())
    if(waterpoll(wschannel) == False):
        print("Watering Initiated!")
        water_plant(RELAY, SECONDS_TO_WATER)

 
#GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)  # let us know when the pin goes HIGH or LOW
#GPIO.add_event_callback(channel, callback)  # assign function to GPIO PIN, Run function on change
 
# infinite loop

  
  
# TEMP AND HUMID SENSOR CODE


# SPDX-FileCopyrightText: 2017 Limor Fried for Adafruit Industries
#
# SPDX-License-Identifier: MIT

import time

import adafruit_dht
import board

dht = adafruit_dht.DHT22(board.D4)

while True:
    time.sleep(1)
    main()

    try:
        temperature = dht.temperature
        humidity = dht.humidity
        # Print what we got to the REPL
        print("Temp: {:.1f} *C \t Humidity: {}%".format(temperature, humidity))
    except RuntimeError as e:
        # Reading doesn't always work! Just print error and we'll try again
        print("Reading from DHT failure: ", e.args)

    time.sleep(1)
