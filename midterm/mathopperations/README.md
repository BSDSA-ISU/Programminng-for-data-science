# the building blocks of computations

- symbols used to perform mathemaical operations between values(called operands)
- they allow python to funcion like a powerful calculator
- Calculating total price to determine the average of a set of numbers, they are fundamental

## two types of division

1. **Floathing-point division (/)**
    - the standard division operator
    - always float
2. **integer (Floor) Division (//)**
   - Returns the quotient, discarding any remainder.
   - Rounds the result down to the nearest whole number.
   - 10 // 3 returns 3.

code example:

```python
print(10 / 3) # 3.3333333__
print(10 // 3) 3 3
```

## Power and in-place Operations

**Exponentiation (\*\*)**

- Raises the first number to the power of the second.
- 2 ** 3 means $2^3$, which is 8.
- 5 ** 2 means $5^2$, which is 25.

**in place Operators (+=, -=, \*=, etc)**:

- a shortcut for performing an operation on a variable and then assigning the result back to he same variable.
- They make code more concise.

Code Example:

```python
# Exponentiation
print(2 ** 4) # 16
print(3 ** 2) # 9

# in place Operators
count = 5
count += 2 # same as count = count + 2
print(count) # 7
total = 10
total *= # same as total = total * 3
print(total)
```

## the order of operations

Python doesn't calculate from left to right; it follows a specific rule set called operator precedence.

Remmber the acronym **PEMDAS**:

- Parentheses: ()
- exponents \*\*
- Multiplication *, Division /, //,
- modulus %
- addition +, Subtraction

Code Example:

```python
result = 10 + 3 * 2 ** 2
# step 1: 2 ** 2
# step 2: 3 * 2
# step 3: 10 + 3
```

Code example 2:

```python
\
```

## real world example

A great example using integer division (//) and mdulus (%) together.

**code example**:

```python
total_seconds = 367

# Calculate minutes and seconds
minutes = total_seconds // 60 # how many whole mintues
seconds = total_seconds % 60 # how many seconds are left over?

print(f"{total_seconds} seconds is {minutes} minutes and {seconds} seconds")
```

## Summary & best practices

- Arithmetic operaions (+, -, *, /, %, **, //) are used for mathematical calculations
- know the difference between / and // (integer division).
- operator precedence (**PEMDAS**) dictates the order of calculations.
- use parentheses **()** to clarify complex rxpressions and force a specific order.
- in place operations (*=, += etc...)
  
## practice

Challenge: write a short program that takes a number of inhes as input and converts it to feet and inches

Hint: 1 foot = 12 inches. use // and %
