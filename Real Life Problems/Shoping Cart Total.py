num= int(input("How many Product do you buy?:"))
total=0
for price in range (num):
    price=int(input(f"Product {price+1} price: "))
    total +=price
if total>=5000:
    discount=total*(10/100)
    final_price=total-discount

    print("your total price is :" ,total)
    print("Congratulations, you got 10%(",discount,")tk discount on your shoping")

    print("Your Final Price is :" ,final_price)
else:
    print(f"Your total Price is: {total}")
