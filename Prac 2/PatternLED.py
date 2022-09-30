import time, RPi.GPIO as gpio
gpio.setwarnings(False)
gpio.setmode(gpio.BOARD)
gpio.setup(8, gpio.OUT, initial=gpio.LOW)
gpio.setup(11, gpio.OUT, initial=gpio.LOW)
gpio.setup(15, gpio.OUT, initial=gpio.LOW)
while(1):
    gpio.output(8, gpio.HIGH)
    time.sleep(0.5)
    gpio.output(8, gpio.LOW)
    time.sleep(0.5)
    gpio.output(11, gpio.HIGH)
    time.sleep(0.5)
    gpio.output(11, gpio.LOW)
    time.sleep(0.5)
    gpio.output(15, gpio.HIGH)
    time.sleep(0.5)
    gpio.output(15, gpio.LOW)
    time.sleep(0.5)

'''Physical Pin: 8,11,15; Ground : 6 '''