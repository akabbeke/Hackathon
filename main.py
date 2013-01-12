from pymouse import PyMouse
import time


    
import select, socket



def msgDecrypt(msgString):
	#Uses locations of msgString segmentations to breakup into useable data
	m1Loc = [0,1]
	m2Loc = [1,2]
	xLoc = [2,6]
	yLoc = [6,10]
	data = [msgString[m1Loc[0],m1Loc[1]],msgString[m2Loc[0],m2Loc[1]],msgString[xLoc[0],xLoc[1]]]
	return data
	
def ClickHandeler(data,click):
	#This is an ugly function.
	hold = 0
	if(data[0] == 0 and click == 1):
		#If left button has been released
		if(click[4] == 0):
			#If left button was not being held
			m.click(data[2],data[3], 1)
			m.move(data[2],data[3])
	 	if(click[4] == 1):
			#If left button was being held
			m.move(data[2],data[3])
			m.release(data[2],data[3], 1)
	if(data[0] == 1 and click == 1):
		#If left button is being held
		m.press(data[2],data[3], 1)
		m.move(data[2],data[3])
		hold = 1
	if(data[1] == 1):
		#right button pressed
		m.press(data[2],data[3], 2)
		m.move(data[2],data[3])
	else:
		#no buttions pressed move the mouse
		m.move(data[2],data[3])

	
	click2 = data + [ hold ]
	return click2

def Main():
	m = PyMouse() #Instantiate a mouse object
	
	port = 53005  #Where do you expect to get a msg?
	
	bufferSize = 1024 #Whatever you need

	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
	s.sendto('1234', ('<broadcast>', port))
	s.setblocking(0)
	click = [0,0,0,0,0]
	print "Running"
	while True:
		result = select.select([s],[],[])
		msg = result[0][0].recv(bufferSize)
		data = msgDecrypt(msg)
		
		click = ClickHandeler(data,click)

	
if __name__ == "__main__":
    Main()