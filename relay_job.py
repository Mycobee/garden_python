import RPi.GPIO as GPIO
import time

class RelayJob:
	def __init__(self, duration):
		GPIO.setmode(GPIO.BCM)
		GPIO.setwarnings(False)
		GPIO.setup(18,GPIO.OUT)
		self.duration = duration
		
	def triggerRelay(self):
		GPIO.output(18,GPIO.LOW)
		time.sleep(self.duration)
		GPIO.output(18,GPIO.HIGH)
	
	
	
	
