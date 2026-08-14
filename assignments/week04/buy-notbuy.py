"""
ให้รับราคาสินค้าจำนวน 6 รายการเก็บไว้ในตัวแปรชนิด list และรับงบประมาณ "รวม" จากผู้ใช้ 1 ค่า 
จากนั้นให้พิจารณาสินค้าตามลำดับใน list ว่าสามารถซื้อได้หรือไม่ โดยถ้าการซื้อสินค้าชิ้นนั้นแล้วทำให้ยอดใช้จ่ายรวมไม่เกินงบประมาณ 
ให้ถือว่า “buy” และนำราคาสินค้านั้นไปรวมกับยอดใช้จ่าย แต่ถ้าทำให้ยอดรวมเกินงบประมาณ ให้ถือว่า “cannot buy”

ทั้งนี้ให้โปรแกรมขอให้ “พิจารณาตามลำดับใน list” และ “ใช้ยอดสะสมรวมในการตัดสิน” ไม่ใช่ 
"งบต่อชิ้น" แต่เป็นงบทั้งก้อนที่ลดลงเรื่อย ๆ ตามรายการที่ซื้อ

รับราคาสินค้า 6 ค่าและเก็บใน list
รับงบประมาณรวม 1 ค่า
ใช้ loop และ if-else ตรวจสอบราคาสินค้าทีละรายการตามลำดับ
ใช้ตัวแปรสำหรับเก็บยอดใช้จ่ายสะสม
ถ้ายอดใช้จ่ายสะสมบวกกับราคาสินค้าชิ้นปัจจุบันแล้วไม่เกินงบประมาณ ให้แสดงข้อความว่า “buy”
ถ้าเกินงบประมาณ ให้แสดงว่า “cannot buy”
เก็บรายการสินค้าที่ซื้อได้ไว้ใน list ใหม่
แสดงรายการสินค้าที่ซื้อได้ ยอดใช้จ่ายรวม และงบประมาณคงเหลือ

"""
print("Please enter prices of 6 items :")
price_order1 = int(input("item 1 : "))
price_order2 = int(input("item 2 : "))
price_order3 = int(input("item 3 : "))
price_order4 = int(input("item 4 : "))
price_order5 = int(input("item 5 : "))
price_order6 = int(input("item 6 : "))

all_price = [price_order1 ,price_order2 ,price_order3 ,price_order4 ,price_order5 ,price_order6]

budget_price = int(input("\nEnter total budget : "))

total_buy = 0
buy_items = []

for price in all_price:
    if total_buy + price <= budget_price :
        print("can buy : ", price)
        total_buy += price
        buy_items.append(price)
    else:
        print("cannot buy : ", price)

print("\n------------------------------------------------")
print("\nแสดงรายการสินค้าที่ซื้อได้ : ", buy_items)
print("ยอดใช้จ่ายรวม : ", total_buy)
print("งบประมาณคงเหลือ : ", budget_price - total_buy )
