"""
Problem: Major or minor

Read the user's age and print whether they are a minor or an adult.

Requirements:
- Read age with input()
- Convert to int
- If age is not in [0, 120], print 'Invalid age'
- Else if age >= 18, print 'Adult'
- Else print 'Minor'
"""

age = int(input("Enter your age: "))

if age < 0 or age > 120:
    print("Invalid age.")
elif age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")
