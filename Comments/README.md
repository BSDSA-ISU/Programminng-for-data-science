# Introduction to comments

## What are comments?

- Comments = notes written inside code
- Python ignores comment during execution\
- Purpose
  - Explain code for human.
  - MAke debugging easier

## Why use comments?

- Increases code **readability.**
- Makes code **easier to maintain.**
- USeful when working in **teams**.
- Acts as a **reminder** for future you.

## Single line comments

- use the **#** symbol.
- Anything after # is ignored by python.
- example
  
```python
# prints out hello world
print("Hello world")
```

## Multi line comments

- python doesn't have official multi-line comments.
- Conversion: use triple quotes (""" """ or ''' ''')
- Example

```python
"""
This is a comment
here too
"""
```

## when to use single line vs multiple line

- use single line for short notes/
- Use multi-line for detailed explanations or documentation.
- Example: Describing a function's purpose

## Best practices for comments

- Be clear and concise
- Explain **why**, not just what
- Update comments when code changes.
- Avoid redundant or obvious comments.

## Good vs bad comments

- bad example:

```python
# Increase x by 1
x = x + 1
```

- good example:

```python
# Add 1 point to the player's score after a win
x = x + 1
```

## Benefits of commenting

- helps **Collaborators** understand your logic.
- makes debugging faster.
- Acts as **Documentation** for projects.
- Improves **professional coding style**

## common mistake in commenting

- Writing comments that repeat the code.
- Leaving outdated comments.
- Using too many unnecessary comments.
- Not commenting complex logic.

## Summary

- -> single line comment
- """ """ -> Multi-line comments.
- Best practices = clear, concise, updated.
- good comments explain the why
