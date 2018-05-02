from time import sleep
from pyA20.gpio import gpio
from pyA20.gpio import port
motion_s = port.PA12
gpio.init()
gpio.setcfg(motion_s, gpio.INPUT)
try:
    while True:
        state = gpio.input(motion_s)
        sleep(15)
        print(" %d"%state)
except KeyboardInterrupt:
    print("Goodbye.")