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

	def Color(self,r, g, b):
		return ((r  & 0xFF) << 16) | ((g & 0xFF) << 8) | (b & 0xFF)
	
	def stringToBool(self,s):
                if (s == "true"):
                        return True
                else:
                        return False

	def colorwipe(self,perkrat,colorList):
		
		b = self.stringToBool(perkrat)
		if(b):
			for n in range(6):
				for i in range(4):
					curC = self.Color(colorList[i][0],colorList[i][1],colorList[i][2])
					p = (6*i)+n
					self.setpixelcolor(p,curC)
					self.writestrip()
					time.sleep(0.05)
		else: 
		   for i in range(4):
                       	curC = self.Color(colorList[i][0],colorList[i][1],colorList[i][2])
                        for n in range(6):
                                p = (6*i)+n
                                print "p = %s, n= %s, i = %s" % (p,n,i)
                                self.setpixelcolor(p,curC)
		                self.writestrip()
               			time.sleep(0.05)

	
	def allColor2(self,colorList):
	
		for i in range(4):
			curC = self.Color(colorList[i][0],colorList[i][1],colorList[i][2])
			for n in range(6):
				p = (6*i)+n
				print "p = %s, n= %s, i = %s" % (p,n,i)
				self.setpixelcolor(p,curC)
		self.writestrip()
		time.sleep(0.05)
	
	def pixelwipe(self,pk,colorList):
		b = self.stringToBool(perkrat)
		if(b):
		   while(True):
			for n in range(6):
				for i in range(4):
					curC = self.Color(colorList[i][0],colorList[i][1],colorList[i][2])
					p = (6*i)+n
					if(p != 0):
						prev = p-1
						prevC = self.Color(0,0,0)
						self.setpixelcolor(prev,prevC)
					self.setpixelcolor(p,curC)
					self.writestrip()
					time.sleep(0.05)
		else: 
	         while(True):
		   for i in range(4):
                       	curC = self.Color(colorList[i][0],colorList[i][1],colorList[i][2])
                        for n in range(6):
                                p = (6*i)+n
                                if(p != 0):
					prev = p-1
					prevC = self.Color(0,0,0)
					self.setpixelcolor(prev,prevC)
                                print "p = %s, n= %s, i = %s" % (p,n,i)
                                self.setpixelcolor(p,curC)
		                self.writestrip()
               			time.sleep(0.05)
               			
	def allColor(self,pixels,c,wait):
	        for i in range(len(pixels)):
        	         self.setpixelcolor(i,c)
        	self.writestrip()
        	time.sleep(wait)

		
	def rainbow(self):
		r = 255
        	g = 0
        	b = 0
        	for i in range(255):
                 g = i
                 r = 255-i
                 self.allColor(self.ledpixels, self.Color(r,g,b),0.02)
       		for i in range(255):
                 b = i
                 g = 255-i
                 self.allColor(self.ledpixels,self.Color(r,g,b),0.02)
        	for i in range(255):
                 r = i
                 b = 255-i
                 self.allColor(self.ledpixels,self.Color(r,g,b),0.02)


	
	def setpixelcolor(self,n, r, g, b):
		if(n >= len(self.ledpixels)):
			return
		self.ledpixels[n] = Color(r,g,b)

	def setpixelcolor(self,n, c):
		if (n >= len(self.ledpixels)):
			return
		self.ledpixels[n] = c


