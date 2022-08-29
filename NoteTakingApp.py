#Note taking app for Python
#I need to make and create files
import os
import sys
from datetime import *
import calendar
import random
from os.path import exists  # This checks the path and see if it's coming

#Checking file (not sure how it works, checks file location)
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:

        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def createNote():
    print("Stuff has been created")
    pass

def openNote():
    pass

def deleteNote():
    pass
#Create files and a menu:


def main():
    print("Hello! Welcome to my note taking program!")
    print("The options are: \n(Create) Creates a new file \n(Open) Open a new file \n(Delete) Deletes a note")
    List = []
    while True:        
        choice = input("What do you wish to make? ")
        choice.capitalize()
        if choice == "Create":
            createNote()
        elif choice == "Open":
            openNote()
        elif choice == "Delete":
            print("Stuff has been deleted")
            deleteNote
        else:
            print("A correct value has to be given")


if __name__ == "__main__":
    main()
