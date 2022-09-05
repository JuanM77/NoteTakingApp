#Note taking app for Python
#I need to make and create files
from fileinput import filename
import os
import sys
from datetime import *
import calendar
import random
from os.path import exists
from typing import List  # This checks the path and see if it's coming

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
    myList = [] #Sets my List as empty
    nameNoteExists = exists("NameNote.txt")
    if nameNoteExists:
        fhandle_NameNote_r = open("NameNote.txt", "r")
        content_NameNote_r = fhandle_NameNote_r.readlines()#[1:2] check to show from one to length #IMPORTANT
        for line in content_NameNote_r:
           line.strip("\n") #This should strip the \n and leave only the name
           myList.append(line) #appends line to the list

        return myList #Returns the list back to the variable      
    else:
        print("NameNote doesn't exist, creating")
        fhandle_nameNote = open("NameNote.txt", "w")
        fhandle_nameNote.write("NameNote File\n")
        print("NameNote Succefully created! This should only happen once, your program will be closed and reopened")
        input("Press enter to exit")
        sys.exit() #I need to exit since if you keep going it will throw an error
        fhandle_nameNote.close()

 
def createNote(myList):
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
    fhandle_NameNote.write(file_name + "\n")
    myList.append(file_name) #This adds the name of a note if it's created within the program

    #Add way to check if note already exists
    

def accessNote(myList):
    """This function should check at the list with names, and if there is a name in the list, Access the note, else throw an error
    By Accessing a list you can write to it or delete from it"""
    """You can delete it from list by line everytime you add a line it adds a number before it"""  
    def addLine():
        """You input the line you want to add and it adds it"""
        pass
    def deleteLine():
        pass

    name = input("Enter the name of the note you wish to open: ")
    print(myList)
    file_name = name + ".txt"
    print(file_name)
    if file_name in myList:
        print("List found!")
        fhandle_Note = open(file_name, "r")
        content_note = fhandle_Note.readlines()


    

def deleteNote(myList):
    """This function checks the list and if a name is found in the list, delete the note"""
    pass
#Create files and a menu:


def main():
    myList = createNameNote()
    print("")
    print(myList)
    print("")
    print("Hello! Welcome to my note taking program!")
    print("The options are: \n(Create) Creates a new file \n(Access) Access a file \n(Delete) Deletes a note \n(Exit) Exits the program")
    
    while True:        
        choice = input("What do you wish to make? ")
        choice.capitalize()
        if choice == "Create":
            createNote(myList)
        elif choice == "Access":
            accessNote(myList)
        elif choice == "Delete":
            deleteNote(myList)
        elif choice == "Exit":
            print("Exiting program, Thank you!")
            sys.exit()
        else:
            print("A correct value has to be given") 


if __name__ == "__main__":
    main()
