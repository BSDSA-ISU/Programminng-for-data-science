age = 22
is_student = True
has_coupon = False

print(is_student or has_coupon)

if(is_student or has_coupon) and age >= 18:
    print("you are eligible for a discount!")
else:
    print("No chance")