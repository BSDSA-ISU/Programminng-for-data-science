#!/usr/bin/python

Fullname = "Cyrus Troy C. Bazar" # Creates a string variable containing my full name
age = 19 # creates a integer variable
height = 1.67 # creates a float variable containing my height
If_Student = True # variable if I'm an student or not

# add five years to my age
add_five_years = age + 5

# multiply by 100 to convert to cm
height_to_cm = height * 100 # autoconverts to float since height is float: Implicit

print("Welcome to python programming!")
print("Python is widely used in data science, web development, AI and more\n") # print with \n aka newline

print("My name is", Fullname, "\b.")
print("I am", age, "years old", "\b.")
print("My height is", height, "meters", "\b.")
print("I am a student?", If_Student)

print() # simulate a newline

print("Data types:")
print("Fullname is a", type(Fullname), " type") # prints out the data type using the type() function
print("age is a", type(age), " type") # same to all here
print("height is a ", type(height), " type")
print("Fullname is a ", type(If_Student), " type")

print()

print("After 5 years, I will be", add_five_years, "years old")
print("My height in centimeters is", height_to_cm, "cm.")
print("Hello", Fullname, "\b! Nice to meet you.")
print("Is student and over 18?", If_Student)# prints true if above 18

print()

favnumber = input(("Enter your favorite number:")) # get the input from the user
doublefav = int(favnumber) * 2 # converts favnumber string to favnumber if possible else throws exception
print("Double of your number is:",doublefav)
word = input("Enter your favorite word:")
print(word*3) # multiply or double the word

if int(favnumber) == 69 or int(favnumber) == 69420*2:
    print("Nice :D:D:D:D")

