import Minicar
import Adafruit_BBIO.GPIO as GPIO
import time

Car = Minicar.Car()        
Car.Greenlighton()
Car.BothMotorsForward()
time.sleep(2)
Car.Greenlightoff()
Car.Redlighton()
Car.BothMotorsBackward()
time.sleep(2)
Car.Redlightoff()
Car.BothMotorsStop()
GPIO.cleanup()