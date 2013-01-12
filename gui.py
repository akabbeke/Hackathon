import Tkinter
import sys
import server

class simpleapp_tk(Tkinter.Tk):
    def __init__(self,parent):
        Tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.initialize()

    def initialize(self):
        self.grid()

        button = Tkinter.Button(self,text=u"quit",command=self.OnButtonClick)
        button.grid(column=1,row=0)

        self.labelVariable = Tkinter.StringVar()
        label = Tkinter.Label(self,textvariable=self.labelVariable,anchor="w",fg="black",bg="white")
        label.grid(column=0,row=1,columnspan=2,sticky='EW')

        self.grid_columnconfigure(0,weight=1)
        self.resizable(True,False)

    def OnButtonClick(self):
        sys.exit("Program Closed")
def printALot():
		print 'lol'

def main():
	app = simpleapp_tk(None)
	app.title('my application')
	app.after(1000, server.Main)
	app.mainloop()
	

	




if __name__ == "__main__":
	main()
	