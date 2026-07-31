# รับชื่อจริง (หรือข้อความ) จากผู้ใช้
# นับจำนวนสระทั้งหมดในข้อความนั้นว่ามีกี่ตัว (a,e,i,o,u)

# ตัวอย่างหน้าจอ
# what is your name? :boonchoo
# Your text have 4 vowels.

user_name = input("Enter Your name : ")


count = 0
for letter in user_name :
    if letter == 'a' or letter == 'A' :
        count = count + 1
    elif letter == 'e' or letter == 'E' :
        count = count + 1
    elif letter == 'i' or letter == 'I' :
        count = count + 1
    elif letter == 'o' or letter == 'O' :
        count = count + 1
    elif letter == 'u' or letter == 'U' :
        count = count + 1








print(f"ตัวอักษร : {letter}")

print("Your Text Have", count, "vowels")


 