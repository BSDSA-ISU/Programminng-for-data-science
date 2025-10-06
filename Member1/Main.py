#user input
student_name = "Eli" #string variable 
is_student = True  # If he's student
student_age = 19   #integer variable
student_gpa = 1.0  #float variable 
student_course = "bsdsa"   # course variable
student_number = "24-2906" # student number

print("Stored Information")
print("Name:", student_name)  
print("Age:",student_age)       
print("GPA:", student_gpa)
print("Course:", student_course)

#data types 
print("Data Types of Variables")
print("Type of Name")
print(type(student_name))
print(type(student_age))
print(type(student_gpa))
print(type(student_course))
print(type(student_number))

#type conversation 
student_age = 19
student_gpa = 1.0
z = student_age + student_gpa #add
print(z)

if student_gpa <= 3.0 and is_student:
    print(f"{student_name} is passed with the GPA of {student_gpa}")
elif not is_student:
    print(f"{student_name} is not an student")
else:
    print(f"{student_name} is failed")
