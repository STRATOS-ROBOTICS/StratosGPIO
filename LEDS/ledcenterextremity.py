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

#LedPin = 21
#LedPin2 = 17
def setup():
 #   GPIO.setmode(GPIO.BCM)       # Numbers GPIOs by BCM
 #   GPIO.setup(LedPin, GPIO.OUT)   # Set LedPin's mode is output
  #  GPIO.output(LedPin, GPIO.HIGH) # Set LedPin high(+3.3V) to off led
   # GPIO.setup(LedPin2, GPIO.OUT)   # Set LedPin's mode is output
    #GPIO.output(LedPin2, GPIO.HIGH) # Set LedPin high(+3.3V) to off led
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pins, GPIO.OUT)


def loop():
    while True:
        print ("...led on")
   #     GPIO.output(LedPin, GPIO.LOW)  # led on
    #    GPIO.output(LedPin2, GPIO.LOW)  # led on
        GPIO.output(pin07, GPIO.LOW)


        GPIO.output(pin08, GPIO.LOW)
        time.sleep(0.05)

        GPIO.output(pin09, GPIO.LOW)


        GPIO.output(pin06, GPIO.LOW)
        time.sleep(0.05)

        GPIO.output(pin05, GPIO.LOW)


        GPIO.output(pin10, GPIO.LOW)
        time.sleep(0.05)

        GPIO.output(pin04, GPIO.LOW)


        GPIO.output(pin11, GPIO.LOW)
        time.sleep(0.05)

        GPIO.output(pin03, GPIO.LOW)


        GPIO.output(pin12, GPIO.LOW)
        time.sleep(0.05)

        GPIO.output(pin02, GPIO.LOW)

        GPIO.output(pin13, GPIO.LOW)
        time.sleep(0.05)

        GPIO.output(pin14, GPIO.LOW)


        GPIO.output(pin01, GPIO.LOW)
        time.sleep(0.05)

        print ("led off...")
        GPIO.output(pin14, GPIO.HIGH)

        GPIO.output(pin01, GPIO.HIGH)
        time.sleep(0.05)
        GPIO.output(pin13, GPIO.HIGH)

        GPIO.output(pin02, GPIO.HIGH)
        time.sleep(0.05)
        GPIO.output(pin12, GPIO.HIGH)


        GPIO.output(pin03, GPIO.HIGH)
        time.sleep(0.05)

        GPIO.output(pin11, GPIO.HIGH)


        GPIO.output(pin04, GPIO.HIGH)
        time.sleep(0.05)

        GPIO.output(pin10, GPIO.HIGH)


        GPIO.output(pin05, GPIO.HIGH)
        time.sleep(0.05)

        GPIO.output(pin09, GPIO.HIGH)

        
        GPIO.output(pin06, GPIO.HIGH)
        time.sleep(0.05)
        
        GPIO.output(pin08, GPIO.HIGH)


        GPIO.output(pin07, GPIO.HIGH)
        time.sleep(0.05)

        GPIO.output(pin14, GPIO.HIGH)



       





def destroy():
    GPIO.output(pin01, GPIO.HIGH)     # led off
    GPIO.cleanup()                     # Release resource

if __name__ == '__main__':     # Program start from here
    setup()
    try:
        loop()
    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
        destroy()
