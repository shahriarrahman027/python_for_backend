
class_number=int(input("Enter How Many Class held?: "))
present=0
absent=0
for i in range(class_number):
    attendance=input(f"Class {i+1} (P/A):").upper()
    # .upper() converts input to uppercase so both 'p'/'a' and 'P'/'A' are handled correctly

    if attendance=="P":
       present +=1
    elif attendance=="A":
       absent +=1
print(f"Present: {present}")
print(f"Absent:{absent}")
percentage=(present/class_number)*100
print(f"Attendance Percentage: {percentage}%")


