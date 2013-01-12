from pymouse import PyMouse
import time
m = PyMouse()
while True:
	time.sleep(.1)
	print m.position()
