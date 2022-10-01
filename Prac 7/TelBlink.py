'''wget https://raspberrytips.nl/files/tm1637.py
Physical Pin: 8, Ground : 6
'''
import sys, time, datetime, tm1637, RPi.GPIO as gpio, telepot, random

def on(pin):
    GPIO.output(pin, GPIO.HIGH)
    return

def off(pin):
    GPIO.output(pin, GPIO.LOW)
    return

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)

def handle(msg):
    chat_id = msg['chat']['id']
    message = msg['text']
    print (message)

    if message == 'on':
        bot.sendMessage(chat_id, on())
    elif message == 'off':
        bot.sendMessage(chat_id, off())

bot = telepot.Bot('5533229605:AAHO95y82f3PwaXzF8V-Q1DDJYOd9-VCuek')
bot.message_loop(handle)
print('I am listening')

while(1):
    time.sleep(10)
