import tkinter
import tkinter.messagebox
import os



class InputWindow:
    def __init__(self):
        self.main = tkinter.Tk()

        self.top = tkinter.Frame(self.main)
        self.bottom = tkinter.Frame(self.main)

        self.prompt = tkinter.Label(self.top)
        self.entry = tkinter.Entry(self.top)

        self.prompt.pack(side='left')
        self.entry.pack(side='left') 
        
        self.entry.focus()

        self.enter = tkinter.Button(self.bottom, text='Run', command=self.execute)
        self.quit = tkinter.Button(self.bottom, text='Exit', command=self.main.destroy)

        self.enter.pack(side='left')
        self.quit.pack(side='left')

        self.top.pack()
        self.bottom.pack()

        tkinter.mainloop()


    def execute(self):
        state = self.entry.get()
        self.main.destroy()
        os.system('/usr/bin/' + state)


#uncomment to test this individual file
#test = InputWindow()
