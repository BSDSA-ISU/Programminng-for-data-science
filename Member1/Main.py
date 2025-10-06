# Evrein 
# Jl
# Remie Joy
# Jhoana
# Cyrus Troy


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
print("the data type of student_name is",type(student_name))
print("the data type of student_age is", type(student_age))
print("the data type of student_gpa is", type(student_gpa))
print("the data type of student_course is", type(student_course))
print("the data type of student_number is", type(student_number))

#type conversation 
student_age = 19
student_gpa = 1.0
z = student_age + student_gpa #add
print(z)
#Converts students age to float
float(student_age)

if student_gpa <= 3.0 and is_student:
    print(f"{student_name} is passed with the GPA of {student_gpa}")
elif not is_student:
    print(f"{student_name} is not an student")
else:
    print(f"{student_name} is failed")
