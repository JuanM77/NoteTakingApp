#Note taking app for Python
#I need to make and create files
from fileinput import filename
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

def createNameNote():
    nameNoteExists = exists("NameNote.txt")
    if nameNoteExists:
        pass
    else:
        print("NameNote doesn't exist, creating")
        fhandle_nameNote = open("NameNote.txt", "w")
        fhandle_nameNote.write("NameNote")
        print("NameNote Succefully created! This should only happen once")
        input("Press enter to continue")
        fhandle_nameNote.close()


def createNote(List):
    """This function should be able to create a note, add the note to the list and return list with name. 
    IF A NOTE ALREADY HAS THAT NAME it would throw an error"""
    name = input("Enter the name of the note you wish to create: ")
    file_name = name + ".txt"
    input()
    # print(fine_name) Test to see file with .txt was created sucessfully
    fhandle_journal = open(file_name, "w")
    fhandle_journal.write(name)
    print(file_name +  " document successfully created")
    fhandle_journal.close()
    print("Stuff has been created")
    #This section opens the NameNote text file and adds the name of the list
    fhandle_NameNote = open("NameNote.txt", "a+")
    fhandle_NameNote.write(file_name)

    #Add way to check if note already exists
    

def accessNote(List):
    """This function should check at the list with names, and if there is a name in the list, Access the note, else throw an error
    By Accessing a list you can write to it or delete from it"""
    """You can delete it from list by line everytime you add a line it adds a number before it"""  
    def addLine():
        """You input the line you want to add and it adds it"""
        pass
    def deleteLine():
        pass

    name = input("Enter the name of the note you wish to open: ")
    print(List)
    file_name = name + ".txt"
    print(file_name)
    if file_name in List:
        print("List found!")
        fhandle_Note = open(file_name, "r")
        content_note = fhandle_Note.readlines()


    

def deleteNote(List):
    """This function checks the list and if a name is found in the list, delete the note"""
    pass
#Create files and a menu:


def main():
    createNameNote()
    print("")
    print("Hello! Welcome to my note taking program!")
    print("The options are: \n(Create) Creates a new file \n(Access) Access a file \n(Delete) Deletes a note \n(Exit) Exits the program")
    List = []
    while True:        
        choice = input("What do you wish to make? ")
        choice.capitalize()
        if choice == "Create":
            createNote(List)
        elif choice == "Access":
            accessNote(List)
        elif choice == "Delete":
            deleteNote(List)
        elif choice == "Exit":
            print("Exiting program, Thank you!")
            sys.exit()
        else:
            print("A correct value has to be given") 


if __name__ == "__main__":
    main()
