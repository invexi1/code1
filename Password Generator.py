import random
import sys

answer = input("Would you like a password to be randomly generated? Yes or No.  ")
if answer == "no":
        print("Okay :( ")
        sys.exit()
if answer == "No":
        print("Okay :( ")
        sys.exit()
if answer == "yes":
        print("Okay :)")
if answer == "Yes":
        print("Okay:)")




print("Your password is: ")

characters = "qwertyuiopasdfghjklzxcvbnm1234567890!£$%^&*()_+=-@#[]{}<>,.?/|¬`"

password = ""
for x in range(16):
        password += random.choice(characters)

print(password)



