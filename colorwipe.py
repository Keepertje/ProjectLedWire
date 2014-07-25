import RPi.GPIO as GPIO, os, time
from Ledstrip import Ledstrip

GPIO.setmode(GPIO.BCM)

#class ledController

def RCtime(RCpin):
	reading = 0
	GPIO.setup(RCpin, GPIO.OUT)
	GPIO.output(RCpin, GPIO.LOW)
	time.sleep(0.1)
	
	GPIO.setup(RCpin, GPIO.IN)
	while(GPIO.input(RCpin) == GPIO.LOW):
		reading += 1
	return reading

def mapRange(value, leftMin, leftMax, rightMin, rightMax):
	leftSpan = leftMax - leftMin
	rightSpan = rightMax - rightMin
	valueScaled = float(value - leftMin) / float(leftSpan) 	
	return rightMin + valueScaled

def colorwipe(c,delay):
	ledstrip.brightness = 1
	for i in range(25):
		ledstrip.setpixelcolor(i,c)
		ledstrip.writestrip()
		time.sleep(delay)

def allColor(c,delay):
	for i in range(25):
		ledstrip.setpixelcolor(i,c)
	ledstrip.writestrip()
	time.sleep(delay)

def allColor2(colorList):	
	for i in range(4):
		curC = self.Color([i][0],[i][1],[i][2])
		for n in range(6):
			p = (n*i)-(6-n)
			ledstrip.setpixelcolor(p,curC)
	ledstrip.writestrip()
	time.sleep(0.05)
		

if __name__ == "__main__":
	ledstrip = Ledstrip()
	col = ledstrip.Color(255,0,0,0.5)
	col2 = ledstrip.Color(0,255,0,0.5)
	allColor2([[255,0,0],[0,255,0],[0,0,255],[100,100,100]])
	delay = 0.01
	colorwipe(col,0.05)
	brp = 0.5
#	while True:
#		light = RCtime(18)
#		print light
#		br = mapRange(light,200,1000,0,1)
		
	#	diff = int((br*10)-(brp*10))
	#	for i in range(abs(diff)):
	#		if(diff < 0):
	#			colour = ledstrip.Color(255,0,0,brp -( float(i)/float(10) ))
	#		else:
	#			colour = ledstrip.Color(255,0,0,brp + (float(i)/float(10) ))
	#		allColor(colour,0)
	#		time.sleep(0.05)
				
	#	brp = br
	#	time.sleep(5)
		#print br
		#colour = ledstrip.Color(255,0,0, br)
		#allColor(colour, 0) 
	
 
	

