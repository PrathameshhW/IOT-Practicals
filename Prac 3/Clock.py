'''wget https://raspberrytips.nl/files/tm1637.py
Physical: DIO=18, VCC=4, GND=6, CLK=16
'''
import sys, time, datetime, tm1637, RPi.GPIO as gpio
Display = tm1637.TM1637(23,24, tm1637.BRIGHT_TYPICAL)
Display.Clear()
Display.SetBrightnes(1)
while(1):
    now = datetime.datetime.now()
    hour = now.hour
    minute = now.minute
    second = now.second
    currenttime = [int(hour/10), hour%10, int(minute/10), minute%10]
    Display.Show(currenttime)
    Display.ShowDoublepoint(second%2)
    time.sleep(1)