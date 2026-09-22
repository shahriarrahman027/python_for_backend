name=input("Enter Your Name: ")
print(name)
print("Wellcome to SynitySoft")
print(" ")

print(" ")
print("printing the complex version of the age:")
age=20.2j
print("your age is", age,"imagineri part is ",age.imag,"real part is",age.real)

print("S" in name )
print("X" in name )
print("Y" not in name)

print("Conditional Statements")
print(" ")

age=int(input("enter your age:"))

print("your age is "+str(age))
print(" ")
if age>=18 and age<=40:
    print("Your are eligible for the job")
elif age>40 or age<18:
    print("Sorry")
else:
    print("Next time")