from pymouse import PyMouse
import time
m = PyMouse()


def main():
	for counter in range(500):
		m.move(counter,counter)
		time.sleep(1/5)
	print m.screen_size()[0]
def fracToPx(screenFrac):
	m.screen_size()
	
if __name__ == "__main__":
    main()