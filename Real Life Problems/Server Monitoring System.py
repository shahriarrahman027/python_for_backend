# 1. Ask the user to enter CPU usage 10 times.
# 2. For each reading, display its status:
#   * Below 80% → Normal
#   * 80% to 89% → Warning
#   * 90% or above → Critical
# 3. Count how many readings were warnings and how many were critical.
# 4. Display both counts after all 10 readings.
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
