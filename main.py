from character import *
from enemy import *
from combat import *



while True:
    imp = input("Hello, would you like to make a character today, view a list of characters, fight or close? ")
    if imp.lower() == "create":
        character_generator()
    elif imp.lower() == "view":
        character_viewer()
    elif imp.lower() == "fight":
        print("SELECT YOUR CHARACTER!")
        
    elif imp.lower() == "close":
        lc.clearcache()
        break
    else:
        print("Try again.")
