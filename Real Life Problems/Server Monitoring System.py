warning=0
critical=0
for i in range(0,10): 
   use=int(input("Enter Your CUP Usage: "))
   if use<80:
      print("Normal")
   elif 80<=use<=89:
      print("Warning")
      warning+=1
   elif use>=90:
      print("Critical")
      critical+=1
print(f"Warning Alerts: {warning}")
print(f"Critical Alerts: {critical}")
