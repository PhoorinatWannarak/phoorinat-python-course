print("2. Time Converter:")
print("   - Ask user for seconds")
print("   - Convert to hours, minutes, and remaining seconds")
print("   - Example: 3661 seconds = 1 hour, 1 minute, 1 second")
print()

sec = float(input("enter your seconds : "))

hour = sec // 3600
second_remain = sec % 3600
minute = second_remain // 60
second_remain = sec % 60

print(f"{sec} seconds = {hour} hour, {minute} minute , {second_remain} second ")