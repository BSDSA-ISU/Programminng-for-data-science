# Type conversion Simplified

## Types

- Implicit
- Explicit

### Example of use case

- Numeric calculations
- String Calculations
- Data cleaning in analytics

#### Assignment

- Exanple of explicit and implicit

```python
x = "String"

print(x)
```

#### Implicit

```python
x = 10
y = 3.5

# Solve x and y using addition
z = x + y

# print out
print(z)

```

#### Adding bool to int

```python
print(True + 69)
# 70
```

#### Division always result to float

```python
python(5/2)
```

## explicit conversions

- forces the conversion also called type casting

```python
nm_str = "50"
num_int= int(nm_str) + 10
print(num_int)
```

### Why use explicit conversion

- required when python cannot convert automatically

#### Examples

```python

# - Reading numbers from input() to int -> always strings

x = 9
int(x)
float(x)
str(x)

print(bool(0))
print(list([1, 2, 3]))
```

##### Using try exception

```python
try:
    x = input("numbers please\n>>")
    test = int(x)
    print(test)
except Exception:
    print("bobo")

```

### Best practices

- check type before convertion using type()
- Use explicit cnversion for user input
- always expect cnvesion error from external data
- Don't assume all strings are numeric
-x Dont rely on implicit conversion
