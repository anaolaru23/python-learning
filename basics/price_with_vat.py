"""
Problem: Price with VAT

Read a product price and compute VAT (19%) and the final price.

Requirements:
- Read price with input()
- Convert to float
- Compute VAT = 19% of price
- Compute final price = price + VAT
- Print all values formatted with 2 decimals
"""
price = float(input("Enter product price: "))

vat = 0.19 * price
final_price = price + vat

print()
print(f"Price without VAT: {price:.2f} RON")
print(f"VAT (19%): {vat:.2f} RON")
print(f"Final price with VAT: {final_price:.2f} RON")
