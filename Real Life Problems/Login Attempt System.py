for attempt in range (1,4):
    password = input("Enter your password:")
    if password=="admin123":
        print("Log in Succesfull")
        break
else:
    print("Account Blocked")
