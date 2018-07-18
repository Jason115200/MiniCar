import Adafruit_BBIO.GPIO as GPIO
import time

Button1 = "P8_10"
Button2 = "P8_9"
Redlight = "P8_7"
Greenlight = "P8_8"
Motor1enable = "P9_16"
Motor2enable = "P9_14"
Motor1drive = "P8_18"
Motor2drive = "P8_16"

class Car:
    def Greenlighton(self):
        GPIO.output(Greenlight, GPIO.HIGH)

    def Greenlightoff(self):
        GPIO.output(Greenlight, GPIO.LOW)    

    def Redlighton(self):
        GPIO.output(Redlight, GPIO.HIGH)
    
    def Redlightoff(self):
        GPIO.output(Redlight, GPIO.LOW)
    
    def Motor1Forward(self):
        GPIO.output(Motor1enable, GPIO.HIGH)
        GPIO.output(Motor1drive, GPIO.HIGH)
    
    def Motor1Backward(self):
        GPIO.output(Motor1enable, GPIO.HIGH)
        GPIO.output(Motor1drive, GPIO.LOW)

    def Motor1Stop(self):
        GPIO.output(Motor1enable, GPIO.LOW)
        GPIO.cleanup()
        
    def Motor2Forward(self):
        GPIO.output(Motor2enable, GPIO.HIGH)
        GPIO.output(Motor2drive, GPIO.HIGH)
    
    def Motor2Backward(self):
        GPIO.output(Motor2enable, GPIO.HIGH)
        GPIO.output(Motor2drive, GPIO.LOW)

    def Motor2Stop(self):
        GPIO.output(Motor2enable, GPIO.LOW) 
        GPIO.cleanup()

    def BothMotorsForward(self):
        GPIO.output(Motor1enable, GPIO.HIGH)
        GPIO.output(Motor2enable, GPIO.HIGH)
        GPIO.output(Motor1drive, GPIO.HIGH)
        GPIO.output(Motor2drive, GPIO.HIGH)
        
    def BothMotorsBackward(self):
        GPIO.output(Motor1enable, GPIO.HIGH)
        GPIO.output(Motor2enable, GPIO.HIGH)
        GPIO.output(Motor1drive, GPIO.LOW)
        GPIO.output(Motor2drive, GPIO.LOW)
        
    def BothMotorsStop(self):
        GPIO.output(Motor1enable, GPIO.LOW)
        GPIO.output(Motor2enable, GPIO.LOW)
        GPIO.cleanup()

    def __init__(self):
        GPIO.setup(Greenlight, GPIO.OUT)
        GPIO.setup(Redlight, GPIO.OUT)
        GPIO.output(Greenlight, GPIO.HIGH)
        GPIO.output(Redlight, GPIO.HIGH)
        print 'Starting...'
        GPIO.setup(Button1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(Button2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(Motor1enable, GPIO.OUT)
        GPIO.setup(Motor2enable, GPIO.OUT)
        GPIO.setup(Motor1drive, GPIO.OUT)
        GPIO.setup(Motor2drive, GPIO.OUT)
        time.sleep(3)
        GPIO.output(Greenlight, GPIO.LOW)
        GPIO.output(Redlight, GPIO.LOW)
        print 'Ready!'

