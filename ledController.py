from Ledstrip import Ledstrip

class ledController():
	
	def __init__(self):
		ledstrip = Ledstrip()

	def changeColor(r,g,b):
		color = ledstrip.Color(r,g,b,0.5)
		allColor(color,0.5)
		
	def allColor(c,delay):
		for i in range(25):
			ledstrip.setpixelcolor(i,c)
		ledstrip.writestrip()
		time.sleep(delay)

	
