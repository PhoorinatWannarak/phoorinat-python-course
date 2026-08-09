"""

ให้รับคะแนนสอบของนักเรียนจำนวน 5 คนเก็บไว้ในตัวแปรชนิด list 
จากนั้นให้ตรวจสอบคะแนนของนักเรียนแต่ละคนว่าผ่านหรือไม่ผ่าน โดยกำหนดว่าคะแนน 50 คะแนนขึ้นไปถือว่าผ่าน

รับคะแนน 5 ค่า เก็บคะแนนทั้งหมดไว้ใน list (เก็บคะแนนทั้งหมดก่อนค่อยไปตรวจสอบ)
ใช้ loop ตรวจสอบคะแนนทีละค่า (ใช้ "for" loop วน เพื่อการตรวจสอบ)
ใช้ condition (if-else) แสดงผลว่า “ผ่าน” หรือ “ไม่ผ่าน”


"""


student_score1 = int(input("enter student score 1 : "))
student_score2 = int(input("enter student score 2 : "))
student_score3 = int(input("enter student score 3 : "))
student_score4 = int(input("enter student score 4 : "))
student_score5 = int(input("enter student score 5 : "))

all_score = [student_score1,student_score2,student_score3, student_score4, student_score5]

for score in all_score:
    if score >= 50:
        print(score, " --> ผ่าน ")
    else:
        print(score, " --> ไม่ผ่าน ")



print(all_score)