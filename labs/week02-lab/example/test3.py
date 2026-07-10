
# Shopping Calculator Template

item_price = float(input("Enter item price: "))
quantity = int(input("Enter quantity: "))
discount_percent = float(input("Enter discount %: "))
tax_percent = float(input("Enter tax %: "))

# TODO: Calculate subtotal ราคาเต็มเท่าไหร่
subtotal = item_price * quantity

# TODO: Calculate discount amount ได้ส่วนลด
discount = subtotal % (discount_percent / 100)

# TODO: Calculate price after discount ราคาหลังลด
price_after_discount = subtotal - discount 

# TODO: Calculate tax amount ภาษีเท่าไหร่
tax = price_after_discount * (tax_percent  / 100)

# TODO: Calculate final total ต้องจ่ายเท่าไหร่
final_total = price_after_discount + tax

# TODO: Display itemized receipt ออกจากทางหน้าจอ

print("subtotal = ", subtotal)
print("discount = ", discount)
print("price_after_discount = " ,price_after_discount)
print("tax = " , tax)
print(f"final_total = ", final_total)
 








