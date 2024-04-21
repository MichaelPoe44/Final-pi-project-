import hashlib

#for add method
#Michael = hashlib.new("SHA256",b"1234")

Michael = hashlib.new("SHA256")
Michael.update(b"1985")

print(Michael.hexdigest())

#want to have a list of hashed passwords
#can take a new str and hash it then store it in the list

#a function to take pass hash it then store it activated by a button in  
    #gui only after someone has put in a correct pass


class Users:
    def __init__(self):
        self.dict = {"Michael":"78e370b587b145920213731b7c7c725e512b3b6577c51c800218a7c764c532ae"}
        self.counter = 1
    
    def add(self,input:str):
        guest = hashlib.new("SHA256",input)
        self.dict["guest"+str(self.counter)] = guest





