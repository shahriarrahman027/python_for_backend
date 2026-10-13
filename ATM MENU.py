# log in System
# check Balance 
# Deoposit 
# withdraw 
# Exit

print("Welcome to XYZ Bank")
print("1.Log in")
option=int(input("Enter your option: "))
if option == 1:
    for i in range(1,4):
        password=input("Enter your password: ")
        if password == "afeenolove123":
            print("Log in successfully")
            print("Welcome to XYZ Bank")
        print("1.Check Balance")
        print("2.Deposit")
        print("3.Withdraw")
        print("4.Exit")
        option2=int(input("Enter your option: "))
        balance = 10000
        if option2==1:
            print("Your Current Balance is :", balance)
        elif option2==2:
            deposit=int(input("Enter Your Deposite Ammount:"))
            balance+=deposit
            print("Deposite Succesfull")
        elif option2==3:
            withdraw=int(input("Enter Your Withdraw Ammount:"))
            balance -= withdraw
        elif option2==4:
            print("Have a nice day")
    else:
        print("Account Blocked")
        


