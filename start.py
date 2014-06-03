import json
import time

from flask import Flask, flash,session,request, url_for, redirect, render_template, abort, g, jsonify

app = Flask(__name__)
app.config.from_object(__name__)
app.debug = True

@app.route('/')
def index():
	return render_template('index.html')

if __name__ == '__main__':
	app.run()

# Stolen from http://stackoverflow.com/questions/4296249/how-do-i-convert-a-hex-triplet-to-an-rgb-tuple-and-back
# turn rgb to hex and vice versa

HEX = '0123456789abcdef'
HEX2 = dict((a+b, HEX.index(a)*16 + HEX.index(b)) for a in HEX for b in HEX)

def rgb(triplet):
    triplet = triplet.lower()
    return { 'R' : HEX2[triplet[0:2]], 'G' : HEX2[triplet[2:4]], 'B' : HEX2[triplet[4:6]]}

def triplet(rgb):
    return format((rgb[0]<<16)|(rgb[1]<<8)|rgb[2], '06x')

#read hex_value send from website
#convert to rgb
#why does print not work?
#todo: send rgb to led strip. 

@app.route('/set/<hex_value>', methods = ['GET','POST'])
def send_color(hex_value):
	rgb_v = rgb(hex_value)
	print "Hello world"	
#print 'Red %s Green %s Blue %s' % (rgb_value['R'], rgb_value['G'], rgb_value['B'])	

#add brightness
