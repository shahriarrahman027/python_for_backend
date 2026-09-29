withdrawal = int(input("How many money do you want to withdraw?:"))
balance=10000;
if balance>=withdrawal & withdrawal>0:
    balance=balance-withdrawal
    print(withdrawal,"tk withdraw successful")
    print()
    print("New Balance is:", balance )
elif balance<withdrawal:
    print("You Haven't enough sufficient money to withdraw")
else:
    print("Invalid Amount. Please Try Again")
