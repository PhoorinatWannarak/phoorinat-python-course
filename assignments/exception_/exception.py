
num1 = int(input(" ตัวเลขที่ 1 : "))
num2 = int(input(" ตัวเลขที่ 2 : "))
oper = input(" เครื่องหมาย + , - , * , / : ")

try :
    if oper == "+" :
        result = num1 + num2 
    elif oper == "-" :
        result = num1- num2
    elif oper == "*" :
        result = num1 * num2
    elif oper == "/" :
        reslt = num1 / num2
    else:
        raise ValueError("เครื่องหมายต้องเป็น + - * / เท่านั้น")

    print(f"{num1} {oper} {num2} = {result}")

except ValueError:
    print("กรุณากรอกข้อมูลที่เป็นตัวเลขเท่านั้น")

except ZeroDivisionError:
    print("ไม่สามารถหารด้วยศูนย์ได้")

except Exception:
    print("มีบางอย่างผิดพลาดแต่ไม่รู้ตรงไหน")

else: 
    print("คำนวณข้อมูลเรียบร้อยแล้ว")

finally:
    print("จบการทำงาน")

