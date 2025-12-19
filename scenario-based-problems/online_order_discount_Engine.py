total_order_amount = int(input("Enter the total order amount: "))

final_amount = total_order_amount
if total_order_amount >= 5000:
    discount_price  = final_amount - (final_amount * 0.20)
    final_amount = discount_price
elif total_order_amount >= 3000:
    discount_price = final_amount - (final_amount * 0.10)
    final_amount = discount_price
elif total_order_amount >= 1000:
    discount_price = final_amount - (final_amount * 0.05)
    final_amount = discount_price
else:
    print("You have no discount")
    
print(final_amount)