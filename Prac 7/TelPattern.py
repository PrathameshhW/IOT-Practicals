'''wget https://raspberrytips.nl/files/tm1637.py
Physical Pin: 8,11,15; Ground : 6
'''
import sys, time, datetime, tm1637, RPi.GPIO as gpio, telepot, random

def on(pin):
    GPIO.output(pin, GPIO.HIGH)
    return

def off(pin):
    GPIO.output(pin, GPIO.LOW)
    return

GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)

def handle(msg):
    chat_id = msg['chat']['id']
    message = msg['text']
    print (message)

    if message == 'on':
        bot.sendMessage(chat_id, on(8), time.sleep(0.2), on(11), time.sleep(0.5), on(15))
    elif message == 'off':
        bot.sendMessage(chat_id, off(8), time.sleep(0.2), off(11), time.sleep(0.5), off(15))

bot = telepot.Bot('YOUR BOT TOKEN')
bot.message_loop(handle)
print('I am listening')

while(1):
    time.sleep(10)
