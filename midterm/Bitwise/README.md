# Bitwise Operation in Python

> Working with the 0s and 1s

- [Bitwise Operation in Python](#bitwise-operation-in-python)
  - [Learning content](#learning-content)
  - [The language of Computers: Binary](#the-language-of-computers-binary)
  - [Meet the Bitwise Operators](#meet-the-bitwise-operators)
  - [Operators Deep Dive: AND(\&) and OR(|)](#operators-deep-dive-and-and-or)
  - [Operator Deep Dive: XOR(^) \& NOT(~)](#operator-deep-dive-xor--not)
  - [Operator deep dive: Shifts (\<\<, \>\>)](#operator-deep-dive-shifts--)
  - [Practical Application 1: Network Masks \& Permissions](#practical-application-1-network-masks--permissions)
  - [Practical Application 2: Simple Encryption \& Parity Checks](#practical-application-2-simple-encryption--parity-checks)
  - [Performance and when to use them](#performance-and-when-to-use-them)
  - [Summary \& Key Takeaway](#summary--key-takeaway)

## Learning content

- **The Binary Basics**: How computers represent
integers.
- **The Operators Themselves**: &, |, ^, ~, <<, >> Why Should I Care? Practical, real-world applications.

## The language of Computers: Binary

Computers store everything as bits - fundamental units of data that can be either 0(off) and and 1(on)

An integer, like 5 is store as a sequence of bits. for example 5 is 101 in binary.

$1*2^2 + 0*2^1 + 1*2^0 = 4 + 0 + 1 = 5$

**12**:

$1 \ 1 \ 0 \  0$

Python's bin() function lets us see this representation.

```python
# Example: Binary Representation
num = 5

print(bin(num))
# The '0B' represents binary
```

## Meet the Bitwise Operators

Bitwise operators work directly on the bits of integers, comparing them one position at a time

| Operator | Name | Description |
|  -----   | ---- |   ---       |
|   &      | AND   |   Both bits must be 1 |
|  '       | OR    |  At least one bit is 1 |
|   ^      | XOR   | Exactly one bit is 1   |
|   ~      | NOT   | Flips all the bits   |
| <<       | Left Shift | Shifts bits to the left |
| >>       | Right Shift | Shifts bits to the right |

## Operators Deep Dive: AND(&) and OR(|)

- **AND(&&)**: Result is 1 only if both bits are 1.
- **OR(|)**: Result is 1 at lest one bit is 1.

```python
a = 10 # Binary: 1010
b = 4 # Binary: 0100

print(a & b) # 0 (0000) - No bits are 1 in both.
print(a | b) # 14 (1110) - Bits are 1 in one or the other
```

## Operator Deep Dive: XOR(^) & NOT(~)

- **XOR**: Result is 1 only the bits are different.
- **NOT(~)**: Flips every bit.

```python
a = 10 # binary: ...001010
b = 4 # binary: ...000100
print(a ^ b) # 14 (1110) - Bits are different.
print(~a) # -11 (...110101) - Flips all bits.
```

## Operator deep dive: Shifts (<<, >>)

- **Left Shift (<<):** Shifts bits left, filling the vacated bits with 0. Effectively multiplies by 2ⁿ.
- **Right Shift (>>):** Shifts bits right. Effectively divides by 2ⁿ (floor division).

$$
\text{example}
$$
$$
for \ 5 \  and \ 2
$$

```python
print(a << 1) # 10 (1010) -> 5 * 2¹ = 10
print(a << 2) # 20 (10100) -> 5 * 2² = 20
print(a >> 1) # 2 (10) -> 5 // 2¹ = 2
print(a >> 2) # 1 (1) -> 5 // 2² = 1
```

## Practical Application 1: Network Masks & Permissions

Network Subnet Masks: IP addresses use bitwise AND
with a subnet mask to determine the network portion.

- IP: 192.168.1.10 & Mask: 255.255.255.0 = Network: 192.168.1.0

Permissions Systems (Like Unix file perms): Use bits
to represent Read, Write, Execute.

- READ = 4 (100), WRITE = 2 (010), EXECUTE = 1 (001) User permissions: READ | WRITE = 6 (110)

```python
READ = 0b100 # 4
WRITE = 0b010 # 2
EXECUTE = 0b001 # 1
my_perm = READ | WRITE # I have read and write (110 = 6)
can_read = (my_perm & READ) == READ # True
```

## Practical Application 2: Simple Encryption & Parity Checks

Simple XOR Encryption: XOR a number with a "key" to
encrypt, then XOR again to decrypt!

- data ^ key = encrypted_data
- encrypted_data ^ key = data (It reverses itself!)

```python
# Simple Toggle/Encryption
secret = 42
key = 123
encrypted = secret ^ key # Jumbles the value

print(encrypted) # 81
decrypted = encrypted ^ key
print(decrypted) # 42 (The original secret!) Parity Check: Use XOR to quickly check if the number of 1-bits is even or odd
```

## Performance and when to use them

- Extremely fast: Bitwise operations are among the fastest operations a CPU can perform.
- memory efficient: Can pick multiple True/False "flags" into a single integer:
- Use cases
  - **Low level programming**: Device drivers, embedded systems
  - **PErformance critical side:** algorithms in graphics. cryptography, and compression.
  - **Competitive Programming:** For elegant and fast solutions.
- **Warning:** Prioritize readability over "clever"
bitwise tricks in most business application

## Summary & Key Takeaway

- Bitwise operators (&, |, ', ~, <<, >>) work on the binary representation
- They are powerful tools for direct bit
manipulation.
- Key Applications: Network masks, permission
systems, simple encryption, and performance
optimization.
- Use bin() to visualize what's happening at the
bit level.
- While powerful, always consider code clarity
for your audience.
