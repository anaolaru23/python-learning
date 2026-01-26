"""
Problem: Age from birth year

Read a birth year from the user and compute the user's age.
Assume the current year is 2026.

Requirements:
- Use input()
- Convert the value to int (typecasting)
- If birth year > 2026, print an error message
- Otherwise, print the age
"""

birth_year = int(input("Enter your birth year: "))

if birth_year > 2026:
    print("Invalid birth year.")
else:
    age = 2026 - birth_year
    print(f"Your age is {age} years.")
