from tkinter import *
from time import sleep
from Hashing import Users

#
# from gpiozero import Servo
# from time import sleep
# servo = Servo(18)
# 

#The passcodes to unlock the box (are stored in the Users class in "Hashing.py")
PASSWORDS = Users()
#This needs to be the length of the passwords intended on using
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
        self.creating_new_user = False



        
        #sets up buttons and display
    def setupLayout(self):
        self.pack(fill=BOTH,expand=1)
        self.display = Label(self,text="",font=("TextGyreAdventor", 45),height=1,width=9,anchor=E)
        self.display.grid(row=0,column=0,columnspan=4,sticky=E+W+N+S)
        self.info = Text(self,bg="lightgrey",fg="black",state=NORMAL,yscrollcommand=Scrollbar,height=31)
        self.info.grid(row=0,column=4,columnspan=1,rowspan=4)
        self.info.grid_propagate(True)
        self.display.focus()

        
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

       
        img = PhotoImage(file='images/Lock.gif')
        button = Button(self,image=img,bg="white",borderwidth=0,highlightthickness=0,activebackground="white",command=lambda:self.process("Lock"))
        button.image = img
        button.grid(row=2 ,column=3,sticky=N+S+E+W )
        
        button = Button(self,bg="blue",text="Enter",font=("TextGyreAdventor", 20),borderwidth=0,highlightthickness=0,activebackground="white",command=lambda:self.process("Enter"))
        button.grid(row=4,column=0,sticky=N+S+E+W,columnspan=2,ipady=30)

        button = Button(self,bg="blue",text="Create\n Guest",font=("TextGyreAdventor", 20),borderwidth=0,highlightthickness=0,activebackground="white",command=lambda:self.process("new_user"))
        button.grid(row=3,column=3,sticky=N+S+E+W)

    #for if access is granted
    def AccessGranted(self,name):
        print("Access Granted")
        self.display.config(background="green")
        self.display["text"] = "Access Granted"
        self.info.insert("1.0",f"box unlocked {name} \n")
        # servo.min()

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
        # servo.max()
        window.after(1000,self.clear)
        self.info.insert("1.0","box locked\n")
        
    
    #for the after funct in the lock funct to clear the display
    def clear(self):
        self.display["text"] = ""



    #processes the button pressed
    def process(self,buttonNum):
        if self.shouldClear == True:
            self.display.config(background="lightgrey")
            self.display["text"] = ""
            self.typed = ""
            self.shouldClear = False
        
        if buttonNum == "Lock":
            ##add to the lock fuction 
            self.lock()
            self.shouldClear = True


        if buttonNum == "new_user":
            temp = PASSWORDS.turn_hash(self.typed)
            key = PASSWORDS.find(temp)
            if key in PASSWORDS.admins:
                self.creating_new_user = True
                self.creator = key
                self.display["text"] = "Guest Password:"
                

            else:
                self.display.config(background="red")
                self.display["text"] = "Admins Only"
            self.shouldClear = True
            



        
        elif buttonNum == "Enter":
            #if not creating a new user
            #turns the current input on keypad into a hash and compares 
            #if it matches one in the stored users dictionary
            if not self.creating_new_user:
                temp = PASSWORDS.turn_hash(self.typed)
                key = PASSWORDS.find(temp)
                if key:
                    self.AccessGranted(key)
                    print("unlocked")
                else:
                    self.AccessDenied()
            #if creating a new user will create a guest user
            #but the pass must be 4 digits
            if self.creating_new_user:
                if len(self.typed)==4:
                    PASSWORDS.add(self.typed)
                    self.info.insert("1.0",f"Guest{PASSWORDS.counter-1} granted access by {self.creator}\n")
                    
                    self.creating_new_user = False
                else:
                    self.display.config(background="red")
                    self.display["text"] = "Invalid Password"
                    # self.creating_new_user = False

            self.shouldClear = True
            

        #takes away the last typed number on keypad
        elif buttonNum == "back":
            self.display["text"] = self.display["text"][0:-1]
            self.typed = self.typed[0:-1]

        #adds the number typed onto the keypad
        elif len(self.display["text"])<LENGTH_PASS:
            self.typed += buttonNum
            self.display["text"]+="*"
        
        print(self.typed)
        print(PASSWORDS.dict.keys())







#passwords:
# Michael: 1985
# Jayden: 7541
# Satyendra: 6243



window = Tk()
window.title("Keypad")
#window.geometry("700x500")
gui = Gui(window)
window.mainloop()
