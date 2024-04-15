from tkinter import *
from time import sleep

#
from gpiozero import Servo
from time import sleep
servo = Servo(18)
# 

#The passcode to unlock the box
PASSWORD = "1985"
#This needs to be the length of the password
LENGTH_PASS = 4






class Gui(Frame):
    def __init__(self,container):
        Frame.__init__(self,container,bg="white")
        self.setupLayout()
        self.lockStatus = "Locked"
        #is what the user has typed in as a passcode
        self.typed = ""
        #decides if the display should be cleared
        self.shouldClear = False
        
        #sets up buttons and display
    def setupLayout(self):
        self.pack(fill=BOTH,expand=1)
        self.display = Label(self,text="",font=("TextGyreAdventor", 45),height=1,width=9,anchor=E)
        self.display.grid(row=0,column=0,columnspan=10,sticky=E+W+N+S)
        
        img = PhotoImage(file='images/1.gif') 
        button = Button(self,image=img,bg="white",borderwidth=0,highlightthickness=0,activebackground="white",command=lambda:self.process("1")) 
        button.image = img
        button.grid(row=1 ,column=0,sticky=N+S+E+W ) 

        img = PhotoImage(file='images/2.gif') 
        button = Button(self,image=img,bg="white",borderwidth=0,highlightthickness=0,activebackground="white",command=lambda:self.process("2")) 
        button.image = img
        button.grid(row=1 ,column=1,sticky=N+S+E+W )

        img = PhotoImage(file='images/3.gif')
        button = Button(self,image=img,bg="white",borderwidth=0,highlightthickness=0,activebackground="white",command=lambda:self.process("3"))
        button.image = img
        button.grid(row=1 ,column=2,sticky=N+S+E+W)

        img = PhotoImage(file='images/4.gif')
        button = Button(self,image=img,bg="white",borderwidth=0,highlightthickness=0,activebackground="white",command=lambda:self.process("4"))
        button.image = img
        button.grid(row=2 ,column=0,sticky=N+S+E+W)

        img = PhotoImage(file='images/5.gif')
        button = Button(self,image=img,bg="white",borderwidth=0,highlightthickness=0,activebackground="white",command=lambda:self.process("5"))
        button.image = img
        button.grid(row=2 ,column=1 ,sticky=N+S+E+W)

        img = PhotoImage(file='images/6.gif')
        button = Button(self,image=img,bg="white",borderwidth=0,highlightthickness=0,activebackground="white",command=lambda:self.process("6"))
        button.image = img
        button.grid(row=2 ,column=2,sticky=N+S+E+W )

        img = PhotoImage(file='images/7.gif')
        button = Button(self,image=img,bg="white",borderwidth=0,highlightthickness=0,activebackground="white",command=lambda:self.process("7"))
        button.image = img
        button.grid(row=3 ,column=0,sticky=N+S+E+W)

        img = PhotoImage(file='images/8.gif')
        button = Button(self,image=img,bg="white",borderwidth=0,highlightthickness=0,activebackground="white",command=lambda:self.process("8"))
        button.image = img
        button.grid(row=3 ,column=1,sticky=N+S+E+W )

        img = PhotoImage(file='images/9.gif')
        button = Button(self,image=img,bg="white",borderwidth=0,highlightthickness=0,activebackground="white",command=lambda:self.process("9"))
        button.image = img
        button.grid(row=3 ,column=2,sticky=N+S+E+W )

        img = PhotoImage(file='images/bak.gif')
        button = Button(self,image=img,bg="white",borderwidth=0,highlightthickness=0,activebackground="white",command=lambda:self.process("back"))
        button.image = img
        button.grid(row=1 ,column=3,sticky=N+S+E+W )

       
        img = PhotoImage(file='images/eql.gif')
        button = Button(self,image=img,bg="white",borderwidth=0,highlightthickness=0,activebackground="white",command=lambda:self.process("Lock"))
        button.image = img
        button.grid(row=2 ,column=3,sticky=N+S+E+W )
        
        button = Button(self,bg="blue",text="Enter",font=("TextGyreAdventor", 20),borderwidth=0,highlightthickness=0,activebackground="white",command=lambda:self.process("Enter"))
        button.grid(row=3,column=3,sticky=N+S+E+W )


    #for if access is granted
    def AccessGranted(self):
        print("Access Granted")
        self.display.config(background="green")
        self.display["text"] = "Access Granted"
        servo.min()

    #for if access is denied  
    def AccessDenied(self):
        print("Access Denied")
        self.display.config(background="red")
        self.display["text"] = "Access Denied"
        

    #locks the box
    def lock(self):
        self.typed = ""
        self.display["text"] = "Locking..."
        print("Locking...")
        servo.max()
        window.after(1000,self.clear)
        
    
    #for the after funct in the lock funct to clear the display
    def clear(self):
        self.display["text"] = ""



    #processes the button pressed
    def process(self,buttonNum):
        if self.shouldClear == True:
            self.display.config(background="white")
            self.display["text"] = ""
            self.typed = ""
            self.shouldClear = False
        
        if buttonNum == "Lock":
            #add to the lock fuction 
            self.lock()
            self.shouldClear = True

        if buttonNum == "Enter":
            if self.typed == PASSWORD:
                self.AccessGranted()
                self.shouldClear = True
            else:
                self.AccessDenied()
                self.shouldClear = True

        elif buttonNum == "back":
            self.display["text"] = self.display["text"][0:-1]
            self.typed = self.typed[0:-1]

        elif len(self.display["text"])<LENGTH_PASS:
            self.typed += buttonNum
            self.display["text"]+="*"
        
        print(self.typed)





window = Tk()
window.title("Keypad")
#window.geometry("700x500")
gui = Gui(window)
window.mainloop()
