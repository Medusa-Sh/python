#create class
class IOSstring():

    #constructor to set default value
    def __init__(self):
        self.string=""

    #function to get input from user
    def get_string(self):
        self.string=input("Enter a string: ")

    #function to print the string in uppercase
    def print_upper(self):
        print("Result is:",self.string.upper())
    #object creation
str1=IOSstring()

str1.get_string()
str1.print_upper()