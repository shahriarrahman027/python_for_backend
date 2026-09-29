print()
unit=int(input("How Many Units of Electricity you used?:"))
if 0<unit<=100:
    print("Your bill is :",unit*5,"tk")
elif 100<unit<=200:
    print("Your bill is :",unit*7,"tk")
elif 200<unit<=300:
    print("Your bill is :",unit*10,"tk")
elif unit>300:
    print("Your bill is :",unit*15,"tk")
else:
    print("Invalid Ammount")