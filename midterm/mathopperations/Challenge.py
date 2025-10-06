#Challenge: write a short program that takes a number of cm as input and converts it to feet and inches

# Hint: 1 foot = 12 inches. use // and %

# creating a function for easier understanding
def Number(number : int):
    foot = number // 12
    inch = number % 12
    print(f"{number} cm is: {foot} feet and {inch} inches.")

Number(100)