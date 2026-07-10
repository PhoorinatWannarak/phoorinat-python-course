print("4. BMI Calculator:")
print("   - Ask for weight (kg) and height (m)")
print("   - Calculate: BMI = weight / (height ** 2)")
print()

weight = float(input("enter your weight (kg) : "))
height = float(input("enter your height (m) "))

BMI = weight / (height ** 2)

print(f"BMI = ", BMI)
