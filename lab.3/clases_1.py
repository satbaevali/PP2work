class function:
    def __init__(self):
        self.func=""
    def getstring(self):
        self.func=input("Enter a string:")
    def printString(self):
        print("String is uppercase:",self.func.upper())
        
string_functional=function()
string_functional.getstring()
string_functional.printString()       