import SendMail
import Scheduler

Scheduler.call_repeatedly(10, SendMail.send_email, "dirtyBanana27", "dirtyBanana1234", "dirtybanana27@gmail.com", "Auto mail from Attila.", "Auto mail from Attila.")

from time import sleep
from pyA20.gpio import gpio
from pyA20.gpio import port

import dht11
import time
import datetime

PIN2 = port.PA6
motion_s = port.PA12
gpio.init()
gpio.setcfg(motion_s, gpio.INPUT)


# read data using pin 14
instance = dht11.DHT11(pin=PIN2)

while True:
    result = instance.read()
    if result.is_valid():
        print("Last valid input: " + str(datetime.datetime.now()))
        print("Temperature: %d C" % result.temperature)
        print("Humidity: %d %%" % result.humidity)
        state = gpio.input(motion_s)
        sleep(15)
        print(" %d" % state)

time.sleep(1)

#SendMail.send_email("dirtyBanana27", "dirtyBanana1234", "dirtybanana27@gmail.com", "Auto mail from Attila.", "Auto mail from Attila.")
from time import sleep
from pyA20.gpio import gpio
from pyA20.gpio import port
motion_s = port.PA12
gpio.init()
gpio.setcfg(motion_s, gpio.INPUT)
try:
    while True:
        state = gpio.input(motion_s)
        sleep(1)
        print(" %d"%state)
except KeyboardInterrupt:
    print("Goodbye.")