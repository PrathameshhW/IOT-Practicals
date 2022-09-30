'''wget https://raspberrytips.nl/files/tm1637.py
Physical: DIO=18, VCC=4, GND=6, CLK=16
'''

import sys, time, datetime, tm1637, RPi.GPIO as gpio, telepot, random

def on():
    Display = tm1637.TM1637(23,24, tm1637.BRIGHT_TYPICAL)
    Display.Clear()
    Display.SetBrightnes(1)
    for i in range(10):
        for j in range(10):
            for k in range(10):
                for l in range(10):
                    data = [i,j,k,l]
                    print(data)
                    Display.Show(data)
                    time.sleep(0.02)
    return 'Timer is on'

def off():
    Display = tm1637.TM1637(23,24, tm1637.BRIGHT_TYPICAL)
    Display.Clear()
    Display.SetBrightnes(0)
    return 'Timer is off'

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
print('Ha bol mc!')

while(1):
    time.sleep(1)
    