"""
Problem: Convert minutes to hours and minutes

Read a number of minutes and convert it to hours + remaining minutes.

Requirements:
- Read minutes with input()
- Convert to int
- If minutes < 0, print an error message
- Otherwise:
  - hours = minutes // 60
  - remaining = minutes % 60
  - Print the result (use 'hour' when hours == 1)
"""
total_minutes = int(input("Enter number of minutes: "))

if total_minutes < 0:
    print("Invalid number of minutes.")
else:
    hours = total_minutes // 60
    remaining_minutes = total_minutes % 60

if hours > 1:
    print(f"{hours} hours and {remaining_minutes} minutes")
elif hours == 1:
    print(f"{hours} hour and {remaining_minutes} minutes")
else:
    print(f"{remaining_minutes} minutes")
