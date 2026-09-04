
# รับต่า text จากผู้ใช้
# รับค่าอักขระที่ต้องการค้นหาจากผู้ใช้
# แสดงผลจำนวนของอักขระในข้อความ text

# Insert your text 
# character to find : o
# 5 letter
'''
print("\n=== ITERATING THROUGH STRING ===")
count = 0
text = input("Insert your text : ")
char = input("character to find : ")
for letter in text:
    if letter == char:
        count += 1
print(f"{count} letters char found in '{text}'")

'''

#เขียนโปรแกรมตรวจสอบความแข็งแกร่งของ password
# == มีมากกว่า 8 ตัว / มี @ 1 ตัว / ตัวเลขอักษร

password = input("Insert your password : ")
lenght = len(password)
words = password.split('@')
left = words[0].isalnum()
right = words[1].isalnum()

if len(words) > 1 and password.count("@") == 1:
    left = words[0].isalnum()
    right = words[1].isalnum()
else :
    nothing


test_str = password
print(f"\nValidation methods for '{test_str}':")
print(f"isalnum(): {test_str.isalnum()}")
print(f"isalpha(): {test_str.isalpha()}")
print(f"isdigit(): {test_str.isdigit()}")
print(f"isupper(): {test_str.isupper()}")
print(f"islower(): {test_str.islower()}")

