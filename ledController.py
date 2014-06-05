from Ledstrip import Ledstrip

class ledController():
	
	ledstrip = None
	def __init__(self):
		self.ledstrip = Ledstrip()

	def changeColor(r,g,b):
		color = ledstrip.Color(r,g,b)
		allColor(color)
		
	def allColor(c,delay):
		for i in range(25):
			ledstrip.setpixelcolor(i,c)
		ledstrip.writestrip()
		time.sleep(delay)

	
