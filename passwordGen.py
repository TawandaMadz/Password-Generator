import random
from attr import validate
# from gui import *
from sqlalchemy import false



#password generation characters
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()?"

#Validation for password
valid_low="abcdefghijklmnopqrstuvwxyz"
valid_high="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
valid_num="1234567890"
valid_char="!@#$%^&*()?"


def rety():
    generated = ""
    for i in range(0, 15):
        password = random.choice(letters)
        generated = generated+password
    Validation(generated)

def Validation(password):
    status1=False
    status2=False
    status3=False
    status4 = False
    for x in valid_char:
        for j in password:
           if x == j:
               status1= True
               
               
    for x in valid_high:
        for j in password:
            if x == j:
               status2= True

    for x in valid_num:
        for j in password:
            if x == j:
               status3= True

    for x in valid_low:
        for j in password:
            if x == j:
               status4= True
    if (status1 == True) and (status2 == True) and (status3 == True) and (status4 == True):
        print("Your password is: " + generated)
    else:
        rety()    

#getting num passwords with 15 characters and validating password
num_of_passwords = int(input("How many passwords would you like to generate? "))
for i in range(0, num_of_passwords):
    generated = ""
    for i in range(0, 15):
        password = random.choice(letters)
        generated = generated+password   
    Validation(generated)   


