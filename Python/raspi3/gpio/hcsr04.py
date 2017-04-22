#!/usr/bin/env python
# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time
import sys

def main():
    TRIG = 14
    ECHO = 15
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(TRIG,GPIO.OUT)
    GPIO.setup(ECHO,GPIO.IN)
    GPIO.setwarnings(False)
    while(1):

        GPIO.output(TRIG, GPIO.LOW)
        time.sleep(0.3)
        
        GPIO.output(TRIG, True)
        time.sleep(0.00001)
        GPIO.output(TRIG, False)

        while GPIO.input(ECHO) == 0:
          signaloff = time.time()
        
        while GPIO.input(ECHO) == 1:
          signalon = time.time()

        timepassed = signalon - signaloff
        distance = timepassed * 17000
        print(distance, "cm")
        GPIO.cleanup()
        c = sys.stdin.read(1)
        if c == 's':
            # GPIOピンの設定解除                  
            break
        
if __name__ == "__main__":
    main()
