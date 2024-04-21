import hashlib
from random import randint


#passwords:
# Michael: 1985
# Jayden: 7541
# Satyendra: 6243






class Users:
    def __init__(self):
        self.dict = {"Michael":"78e370b587b145920213731b7c7c725e512b3b6577c51c800218a7c764c532ae",
                     "Jayden":"3728423e108f9a0ace4c9a2409615d1096f9b2fd25b0fec530c48283b075a08a",
                     "Satyendra":"de3ab843c46b152ce475ece30fabbeddde0aceb36329909f14e0b326fcaf4500"
                     }
        self.counter = 1
    

    #a function to take pass hash it then store it activated by a button in  
    #gui only after someone has put in a correct pass
    def add(self,input:str):
        """takes a string and encodes it then stores it in the
            dictionary within Users"""
        #uses SHA256 hashing
        guest = hashlib.new("SHA256")

        #hashes the input
        guest.update(input.encode())

        #adds the guest(with the number of the guest) and the hexidecimal value
        self.dict["guest"+str(self.counter)] = guest.hexdigest()
        self.counter += 1


    #turns the given input into a hashed hexdecimal
    def turn_hash(self,input:str):
        """turns input into a hexidecimal"""
        h = hashlib.new("SHA256")
        h.update(input.encode())
        return h.hexdigest()
    

    def find(self,input):
        """looks to see if the input is a value in the user
            dictionary and returns the key"""
        for key, val in self.dict.items():
            if input == val:
                return key



