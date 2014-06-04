import RPi.GPIO as GPIO, time, os

DEBUG = 1
GPIO.setmode(GPIO.BCM)

class Ledstrip():

	ledpixels = None

	def __init__(self):
		self.ledpixels = [0] * 25

	def writestrip(self):
		spidev = file("/dev/spidev0.0", "w")
		for i in range(len(self.ledpixels)):
			spidev.write(chr((self.ledpixels[i]>>16) & 0xFF))
			spidev.write(chr((self.ledpixels[i]>>8) & 0xFF))
			spidev.write(chr(self.ledpixels[i] & 0xFF))
		spidev.close()
		time.sleep(0.002)

	def Color(self,r, g, b, br):
		return ((int( r * br) & 0xFF) << 16) | ((int(g* br) & 0xFF) << 8) | (int(b* br) & 0xFF)

	def setpixelcolor(self,n, r, g, b, br):
		if(n >= len(self.ledpixels)):
			return
		self.ledpixels[n] = Color(r,g,b,br)

	def setpixelcolor(self,n, c):
		if (n >= len(self.ledpixels)):
			return
		self.ledpixels[n] = c

