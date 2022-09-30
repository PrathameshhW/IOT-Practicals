'''wget https://raspberrytips.nl/files/tm1637.py
Physical: DIO=18, VCC=4, GND=6, CLK=16
'''

import sys, time, datetime, tm1637, RPi.GPIO as gpio
Display = tm1637.TM1637(23,24, tm1637.BRIGHT_TYPICAL)
Display.Clear()
Display.SetBrightnes(1)
while(1):
    temp=[13,14,10,13]
    Display.Show(temp)
    time.sleep(1)