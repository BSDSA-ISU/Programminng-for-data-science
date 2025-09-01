# Type coversion

# types
# Implicit conversion
# Explicit conversion

# Example use cases:
# Numeric Calculations (Implicit)
# String concatenation (Explicit) <-- assignment
# Data cleaning in analytics (Explicit)

# assignment
# example of impliicit and explicit

x = "String"

print(x)

# implicit

x = 10
y = 3.5

z = x+y
print(z) # converts float to int

# adding bool to int
print(True + 5)

# division always result in float:
print(5/2) 

# Explicit conversion
#forces the conversion also called type casting

nm_str = "50"
num_int= int(nm_str) + 10
print(num_int)

# Why use explicit conversion
# required when python cannot convert automatically:
# Examples:
# - Reading numbers from input() to int -> always strings

x = 9
int(x)
float(x)
str(x)

print(bool(0))
print(list([1, 2, 3]))


# USing try exception

try:
    x = input("numbers please \n>>")
    test = int(x)
except Exception:
    print("bobo")

# Best practices 
# check type before convertion using type()\
# Use explicit cnversion for user input
# always expect cnvesion error from external data
# Don't assume all strings are numeric
# Dont rely on implicit conversion

# Visual comparison
# type                             who decide                  example                result
# implicit                            Python                    5 + 2.5                 7.5 float
# explicit                           human                        int("100"                 100 (int)



# 😀😀😀😀😀
