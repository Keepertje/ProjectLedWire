from Ledstrip import Ledstrip

class ledController():
	
	ledstrip = Ledstrip()
	curR = None
	curG = None
	curB = None
	
	def __init__(self):
		ledstrip = Ledstrip()
		curR = 0
		curG = 0
		curB = 0

	def changeColor(self, r,g,b):
		color = ledstrip.Color(r,g,b)
		allColor(color,0.05)
		
	def transision(r,g,b):
		diffR = r - curR
		diffG = g - curG
		diffB = b - curB
		for i in range(abs(diffR)):
			if(diffR > 0):
				changeColor( curR + i,curG,curB)
			else:
				changeColor(curR - i, curG , curB)
		curR = r
		for i in range(abs(diffG)):
			if(diffG > 0):
				changeColor( curR ,curG + i,curB)
			else:
				changeColor(curR - i, curG - i, curB)
		curG = g
		for i in range(abs(diffB)):
			if(diffB > 0):
				changeColor(curR,curG,curB + i)
			else:
				changeColor(curR , curG , curB - i)
		curR = b
			
				
		
	def allColor(self, c,delay):
		for i in range(25):
			ledstrip.setpixelcolor(i,c)
		ledstrip.writestrip()
		time.sleep(delay)

	
