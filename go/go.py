import os, sys
import sqlite3
from .db import DB

class Go():

    def __init__(self):
        self.curdir = os.getcwd()

    def help(self):
        try:
            HERE = os.path.abspath(os.path.dirname(__file__)) + "/../help.txt"
            with open(HERE, "r") as helpFile:
                helpText = helpFile.read()
            print(helpText)
            helpFile.close()
        except:
            print("Something went wrong")
        
        
    def add(self, name, dir = None):
        db = DB()
        present = db.find(name)
        if dir is None:
            dir = self.curdir
        elif os.path.isdir(dir) == False:
            print("directory is invalid")
            return    
        if(present > 0):
            print("This name is all ready present")
        else:
            db.entry(dir, name)
            print(dir + " is saved, name = " + name)
        db.close()

    def all(self):
        db = DB()
        data = db.getAll()
        for entry in data:
            print(entry[0] + " " + entry[1])
        db.close()

    def go(self, name):
        db = DB()
        data = db.read(name)
        if data == None:
            print("No such directory in the database \nYou can add it by using go add <name> \nFor more use go help")
        else:
            dir = data[0]        
            os.chdir(dir)
            os.system("start cmd cd {}".format(dir))
        db.close()
        
    def remove(self, name):
        db = DB()
        conformation = db.remove(name)
        if conformation:
            print(name + " have been removed")
        else:
            print(name + " is not present")

