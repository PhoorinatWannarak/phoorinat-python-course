"""
เขียน function แปลงหน่วยสกุลเงิน ที่สามารถแปลงเงินจาก 
THB - USD .. 1 USD = 32 THB
THB - JPY .. 100 JYP = 22 THB

โดยใช้ชื่อและการใช้งาน function convert_currency
(100, "USD)

แสดงผลออกทางหน้าจอ
100 THB = 3.3 USD

และทดสอบการใช้งาน function ที่ตัวเองเขียน
"""

''' def THB_to_USD(THB):
    """Converts THB to USD"""
    USD = THB / 32
    return USD

def USD_to_THB(USD ):
    """Converts USD to THB"""
    THB = USD * 32
    return THB '''



def  convert_currency(a, b):
    """Converts temperature between scales"""
    if b == "USD":
        print(f"{a} THB = {a / 32} USD")
    else:
        print(a, "USD =", a * 32, "THB")

print("Currency Converter:")
convert_currency(100, "USD")
convert_currency(100, "THB")