# Logical operators examples (or, and, not)

# =====================
# OR operator example
# =====================

temp = float(input("The temperature is: "))
is_raining = input("Is it raining? (yes/no): ").lower() == "yes"

if temp >= 35 or temp <= 0 or is_raining:
    print("The outdoor event is cancelled.")
else:
    print("The outdoor event is still scheduled.")

print()

# ==========================
# AND / NOT operators example
# ==========================

temperature = float(input("The temperature is: "))
is_sunny = input("Is it sunny? (yes/no): ").lower() == "yes"

if temperature >= 28 and is_sunny:
    print("It is hot outside.")
    print("It is sunny.")
elif temperature <= 0 and is_sunny:
    print("It is cold outside.")
    print("It is sunny.")
elif 28 > temperature > 0 and not is_sunny:
    print("It is warm outside.")
    print("It is cloudy.")
elif temperature <= 0 and not is_sunny:
    print("It is cold outside.")
    print("It is cloudy.")
else:
    print("The weather is moderate.")
