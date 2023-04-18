from classes import Hardware
from classes import TimeKeeper as TK
#import schedule
import Rpi.GPIO as GPIO
#import smtplib
import time
#import ssl



# WATERING_TIME must be in "00:00:00 PM" format
#WATERING_TIME = '11:59:50 AM'
SECONDS_TO_WATER = 10
RELAY = Hardware.Relay(12, False)
#EMAIL_MESSAGES = {
#    'last_watered': {
#        'subject': 'Raspberry Pi: Plant Watering Time',
#        'message': 'Your plant was last watered at'
#    },
#    'check_water_level': {
#        'subject': 'Raspberry Pi: Check Water Level',
#        'message': 'Check your water level!',
#    }
#}


#GPIO SETUP

wschannel = 13
GPIO.setmode(GPIO.BCM)
GPIO.setup(wschannel, GPIO.IN)
 
def waterpoll(wschannel):
        # for actual plant time should be every few days so 24 * 3600 * 3
        time.sleep(10)
        if GPIO.input(wschannel):
                print("No water Detected!")
                return False
        else:
                print("Water Detected!")
                return True
 
#GPIO.add_event_detect(wschannel, GPIO.BOTH, bouncetime=300)  # let us know when the pin goes HIGH or LOW
#GPIO.add_event_callback(wschannel, callback)  # assign function to GPIO PIN, Run function on change
 
# infinite loop


#def send_email(time_last_watered, subject, message):
#    port = 465
#    smtp_server = "smtp.gmail.com"
#    FROM = TO = "YOUR_EMAIL@gmail.com"
#    password = "YOUR_PASSWORD"
#
#    complete_message = ''
#    if time_last_watered == False:
#        complete_message = "Subject: {}\n\n{}".format(subject, message)
#    else:
#        complete_message = "Subject: {}\n\n{} {}".format(subject, message, time_last_watered)
#    
#    context = ssl.create_default_context()
#    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
#        server.login(FROM, password)
#        server.sendmail(FROM, TO, complete_message)
#
#def send_last_watered_email(time_last_watered):
#    message = EMAIL_MESSAGES['last_watered']['message']
#    subject = EMAIL_MESSAGES['last_watered']['subject']
#    send_email(time_last_watered, subject, message)
#
#def send_check_water_level_email():
#    message = EMAIL_MESSAGES['check_water_level']['message']
#    subject = EMAIL_MESSAGES['check_water_level']['subject']
#    send_email(False, subject, message)
#
def water_plant(relay, seconds):
    relay.on()
    print("Plant is being watered!")
    time.sleep(seconds)
    print("Watering is finished!")
    relay.off()

def main():
    #time_keeper = TK.TimeKeeper(TK.TimeKeeper.get_current_time())
    if(waterpoll(wschannel) == True):
        print("Watering Initiated!")
        water_plant(RELAY, SECONDS_TO_WATER)
        #time_keeper.set_time_last_watered(TK.TimeKeeper.get_current_time())
        #print("\nPlant was last watered at {}".format(time_keeper.time_last_watered))
        # send_last_watered_email(time_keeper.time_last_watered)

# schedule.every().friday.at("12:00").do(send_check_water_level_email)

while True:
    # schedule.run_pending()
    time.sleep(1)
    main()