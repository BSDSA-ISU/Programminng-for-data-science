# activity wtf

- [activity wtf](#activity-wtf)
  - [Part 1: The Arithmetic Operator](#part-1-the-arithmetic-operator)
    - [Task 1: The Basic Calculator](#task-1-the-basic-calculator)
    - [Task 2: The Order of Operations Challenge](#task-2-the-order-of-operations-challenge)
    - [Task 3: Unit Conversion Challenge](#task-3-unit-conversion-challenge)
  - [Part 2: Logical Operator](#part-2-logical-operator)
    - [Task 4: The Movie Ticket Price Decider](#task-4-the-movie-ticket-price-decider)
    - [Task 5: Secure System Login Simulator](#task-5-secure-system-login-simulator)
    - [Challenge Problem (Bonus)](#challenge-problem-bonus)

## Part 1: The Arithmetic Operator

### Task 1: The Basic Calculator

Write a program that does the following:

1. Assigns two different numbers to two variables, a and b.
2. Calculates and prints the result of:

    - Addition (a + b)
    - Subtraction (a - b)
      - Multiplication (a * b)
    - Floating-Point Division (a / b)
    - Integer Division (a // b)
    - Modulus (a % b)
    - Exponentiation (a  b)

Example Output:

```txt
a = 15, b = 4
Addition: 19
Subtraction: 11
Multiplication: 60
Floating-Point Division: 3.75
Integer Division: 3
Modulus: 3
Exponentiation: 50625
```

### Task 2: The Order of Operations Challenge

Without running the code first, predict the output of the following expressions. Then, write a program to check your answers.

1. result1 = 5 + 3 * 2  2
2. result2 = (5 + 3) * 2  2
3. result3 = 10 % 3 + 5 * 2

### Task 3: Unit Conversion Challenge

Write a program that solves the challenge from the presentation.

- Prompt the user to enter a number of inches.
- Convert the input to an integer.
- Calculate how many feet and remaining inches that represents.
- *Hint: Use // for feet and % for inches.*
- Print the result in a user-friendly format.

Example Output:

Enter the number of inches: 47
47 inches is equal to 3 feet and 11 inches.

## Part 2: Logical Operator

### Task 4: The Movie Ticket Price Decider

Write a program that determines the price of a movie ticket based on the following rules:

- Base price is $12.
- Children (age <= 12) get a $3 discount.
- Seniors (age >= 65) get a $4 discount.
- Students (check with a variable is_student) get a $2 discount.

Instructions:

1. Create variables for age and is_student (a boolean).
2. Use logical operators (and, or) and comparison operators (<=, >=) to create the discount rules.
    - *Note: A person can only qualify for one best discount. A 70-year-old student should get the senior discount, not both.*
3. Calculate the final price and print it.

Example Output:

Age: 20
Is student? (True/False): True
Your ticket price is $10.

### Task 5: Secure System Login Simulator

Create a simple login system that checks multiple conditions.

1. Set the correct username, password, and a boolean is_2fa_enabled (Two-Factor Authentication) to True.
2. Prompt the user to enter their input_username, input_password, and input_2fa_code.
3. Assume the correct 2FA code is "123456".
4. The login is successful only if:
    - The username is correct, AND
    - The password is correct, AND
    - (Either the user does not have 2FA enabled OR the entered 2FA code is correct).

Instructions:

- Use and and or operators to combine these conditions in a single if statement.
- Print "Login successful!" or "Login failed!" accordingly.

Example Output:

Enter username: alice
Enter password: wonderland
Is 2FA enabled? (y/n): y
Enter 2FA code: 123456
Login successful!

### Challenge Problem (Bonus)

The Shipping Cost Calculator with Rules
Write a program that calculates shipping costs based on the following complex rules:

- The base shipping cost is $10.
- If the order total weight is over 20 pounds, add $5.
- If the shipping destination is "international", double the total cost.
- However, if the customer is a "premium" member, they get a 20% discount on the final cost and are exempt from the international surcharge.

Instructions:

1. Create variables for weight, destination ("domestic" or "international"), and membership ("standard" or "premium").
2. Use arithmetic operators to calculate the costs.
3. Use logical operators (and, or, not) to check the conditions for the premium member exemption and other rules.
4. Print a detailed breakdown of the final shipping cost.

Example Output:

Weight (lbs): 25
Destination (domestic/international): international
Membership (standard/premium): premium
Final Shipping Cost: $12.00
(Details: Base $10 + Overweight $5, Premium 20% discount applied, International fee waived.)
