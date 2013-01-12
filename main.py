from pymouse import PyMouse
import time

from socket import *

def msgDecrypt(msgString):
	#Uses locations of msgString segmentations to breakup into useable data
	print int(msgString[0:1])
	print int(msgString[1:2])
	print int(msgString[2:6])
	print int(msgString[6:10])
	data = [int(msgString[0:1]),int(msgString[1:2]),int(msgString[2:6]),int(msgString[6:10])]
	return data
	
def ClickHandeler(data,click,m):
	#This is an ugly function.
	hold = 0
	print data[0]
	print click[0]

	
	if(data[0] == 0 and click[0] == 1):
		#If left button has been released
		if(click[4] == 0):
			#If left button was not being held
			m.click(data[2],data[3], 1)
			m.move(data[2],data[3])
			print 'click'
	 	if(click[4] == 1):
			#If left button was being held
			m.move(data[2],data[3])
			m.release(data[2],data[3], 1)
			hold = 0
			print 'unhold'
	
	if(data[0] == 1 and click[0] == 1):
		if(hold==0):
			m.move(data[2],data[3])
		else:
			#If left button is being held
			m.press(data[2],data[3], 1)
			m.move(data[2],data[3])
			hold = 1
			print "holding"
	if(data[1] == 1):
		#right button pressed
		m.press(data[2],data[3], 2)
		m.move(data[2],data[3])
		print "press"
	else:
		#no buttions pressed move the mouse
		print "move"
		m.move(data[2],data[3])

	
	click2 = data + [ hold ]
	return click2


def Main():
	m = PyMouse() #Instantiate a mouse object
	PORT = 11111 # arbitrary, just make it match in Android code
	IP = "192.168.43.199" # represents any IP address

	sock = socket(AF_INET, SOCK_DGRAM) # SOCK_DGRAM means UDP socket
	sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1) # make socket reuseable
	sock.bind((IP, PORT))
	
	click = [0,0,0,0,0]
	print "Running"
	while True:
		data ,shit = sock.recvfrom(1024)
		data = msgDecrypt(data) # blocking
		
		click = ClickHandeler(data,click,m)

	
if __name__ == "__main__":
    Main()