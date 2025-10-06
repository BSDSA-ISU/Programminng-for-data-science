# Logical Operations on python

It’s the topic “Logical operation in Python.”
That refers to using Python’s logical (Boolean) operators — such as:

- **and** → returns True if both operands are true

- **or** → returns True if at least one operand is true

- **not** → reverses the Boolean value (not True → False, and vice versa)
  - but its not the same as != True:

|   Expression | Equivalent | Meaning           |
| ---------- | --------------- | ----------------- |
| `x != 10`  | `not (x == 10)` | Compare directly  |
| `not x`    | `x == False`    | Invert truthiness |

## Usage examples

```python
day = "Saturday"
is_holiday = False

if day == "Saturday" or day == "Sunday" or is_holiday:
    print("It's a day off!")
else:
    print("Its weekday.")
```
