# Making Decisions Smarter: Logical Operators in Python

> Combining Conditions for Complex Logic

## The World of True and False

- Computers make decisions based on Boolean logic:
  - expressions that are either True or False.
- We've seen this in if statements:
  - **if condition.**
- Logical operators allow us to combine these **True/False** values to form more complex conditions.
- They are the **AND**, **OR**, and **NOT** of programming.

Analogy: "I will go to the park if it is sunny
**AND** I have free time."

### The and Operator: All Must Be True

- Returns True only if both operands (conditions) are True.
- If any condition is False, the entire expression is False.
- Think of it as: **"Are condition A and condition B both true?"**

**Code Example:**

```python
age = 25
has_license = True

if age >= 18 and has_license:
  print("You are allowed to drive.")
else:
  print("You cannot drive.")
# Output: You are allowed to drive.
```

### The or Operator: At Least One Must Be True

- Returns True if at least one operand (condition) is True.
- It only returns False if both conditions are False.
- Think of it as: **"Is condition A or condition B true?**"

**Code Example:**

```python
day = "Saturday"
is_holiday = False

if day == "Saturday" or day == "Sunday" or is_holiday:
  print("It's a day off!")
else:
  print("It's a weekday.")
# Output: It's a day off!
```

### The not Operator: The Reverser

- A unary operator (it works on a single condition).
- It reverses, or negates, the Boolean value.
- not True is False.
- not False is True.
- Think of it as: **"Is this condition not true?"**

**Code Example:**

```python
is_raining = False

if not is_raining:
  print("You don't need an umbrella.")
else:
  print("Take an umbrella!")
  # Output: You don't need an umbrella.

user_role = "guest"
if not user_role == "admin":
  print("Access denied.")
  # Checking if a user is NOT an admin
```

### Building Complex Logic

- You can combine **and,** **or**, and **not** to create sophisticated rules.
- Use parentheses () to group conditions and control the order of evaluation (just like in math!).

**Code Example:**

```python
age = 22
is_student = True
has_coupon = False

# Scenario: Discount for students OR anyone with a coupon, but they must be over 18.
if (is_student or has_coupon) and age >= 18:
  print("You are eligible for a discount!")
else:
  print("No discount available.")

# How it evaluates:
# 1. (True OR False) -> True
# 2. (True AND True) -> True
# Output: You are eligible for a discount!
```

**for easy understanding Refer to the truth table:**

| A | B   | A OR B | A AND B | NOT A | NOT B |
|---- | ----- | ------ | ---- | ---- | --- |
| False | False | False  | False | True | True |
| False | True  | True   | False | True | False |
| True  | False | True   | False | False | True |
| True  | True  | True   | True  | False | False |
