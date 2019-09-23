
#!/usr/bin/env python3
import RPi.GPIO as GPIO

import time

pins = [29, 11, 12, 31, 40, 37, 16, 18, 22, 15, 33, 32, 36, 38 ]
pin01 = 29
pin02 = 11
pin03 = 12
pin04 = 31
pin05 = 40
pin06 = 37
pin07 = 16
pin08 = 18
pin09 = 22
pin10 = 15
pin11 = 33
pin12 = 32
pin13 = 36
pin14 = 38

GPIO.setmode(GPIO.BOARD)
GPIO.setup(pins, GPIO.OUT)

GPIO.output(pins, GPIO.LOW)
time.sleep(0.25)
GPIO.output(pins, GPIO.HIGH)
time.sleep(0.25)
GPIO.output(pins, GPIO.LOW)
time.sleep(0.35)
GPIO.output(pins, GPIO.HIGH)
time.sleep(0.25)
GPIO.output(pin01, GPIO.LOW)
time.sleep(0.35)
GPIO.output(pin01, GPIO.HIGH)
time.sleep(0.25)
GPIO.output(pin02, GPIO.LOW)
time.sleep(0.35)
GPIO.output(pin02, GPIO.HIGH)
time.sleep(0.25)
GPIO.output(pin03, GPIO.LOW)
time.sleep(0.35)
GPIO.output(pin03, GPIO.HIGH)
time.sleep(0.25)
GPIO.output(pin04, GPIO.LOW)
time.sleep(0.35)
GPIO.output(pin04, GPIO.HIGH)
time.sleep(0.25)
GPIO.output(pin05, GPIO.LOW)
time.sleep(0.95)
GPIO.output(pin05, GPIO.HIGH)
time.sleep(0.25)
GPIO.output(pin06, GPIO.LOW)
time.sleep(0.35)
GPIO.output(pin06, GPIO.HIGH)
time.sleep(0.25)
GPIO.output(pin07, GPIO.LOW)
time.sleep(0.35)
GPIO.output(pin07, GPIO.HIGH)
time.sleep(0.25)
GPIO.output(pin08, GPIO.LOW)
time.sleep(0.35)
GPIO.output(pin08, GPIO.HIGH)
time.sleep(0.25)
GPIO.output(pin09, GPIO.LOW)
time.sleep(0.35)
GPIO.output(pin09, GPIO.HIGH)
time.sleep(0.25)
GPIO.output(pin10, GPIO.LOW)
time.sleep(0.35)
GPIO.output(pin10, GPIO.HIGH)
time.sleep(0.25)
GPIO.output(pin08, GPIO.LOW)
time.sleep(0.35)
GPIO.output(pin08, GPIO.HIGH)
time.sleep(0.25)
time.sleep(0.25)
GPIO.output(pin11, GPIO.LOW)
time.sleep(0.35)
GPIO.output(pin11, GPIO.HIGH)
time.sleep(0.25)
GPIO.output(pin12, GPIO.LOW)
time.sleep(0.35)
GPIO.output(pin12, GPIO.HIGH)
time.sleep(0.25)
GPIO.output(pin03, GPIO.LOW)
time.sleep(0.35)
GPIO.output(pin03, GPIO.HIGH)
time.sleep(0.25)
GPIO.output(pin13, GPIO.LOW)
time.sleep(1)
GPIO.output(pin13, GPIO.HIGH)
time.sleep(0.25)
GPIO.output(pin14, GPIO.LOW)
time.sleep(0.35)
GPIO.output(pin14, GPIO.HIGH)

