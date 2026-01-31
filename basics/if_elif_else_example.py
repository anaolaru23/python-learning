"""
Example demonstrating if / elif / else statements.
The program calculates ticket price based on age and checks ticket availability.
"""

age = int(input("Enter your age: "))
has_ticket = input("Do you have a ticket? (yes/no): ").lower() == "yes"
price = 10.00

if age >= 65:
    print("You are a senior citizen!")
    print(f"The price for the ticket is ${price * 0.75:.2f}")
elif age >= 18:
    print("You are an adult!")
    print(f"The price for the ticket is ${price:.2f}")
else:
    print("You are a child!")
    print(f"The price for the ticket is ${price * 0.5:.2f}")

if has_ticket:
    print("You may enter, you have a ticket")
else:
    print("You need to buy a ticket!")
