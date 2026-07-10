print("1. Circle Calculator:")
print("   - Ask user for radius")
print("   - Calculate area (π * r²)")
print("   - Calculate circumference (2 * π * r)")
print("   - Use 3.14159 for π")
print()

radius = float(input("enter your radius : "))
area = 3.14159 * radius ** 2
circumference = 2 * 3.14159 * radius

print(f"area = 3.14159 * radius ** 2 = {3.14159} * {radius **2} = {area}")
print(f"circumference = 2 * 3.14159 * radius = {2} * {3.14159} * {radius} = {circumference}")
print()

# print(f"area = {area}, )