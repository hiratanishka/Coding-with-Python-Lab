gpa = float(input("Enter your gpa: "))
attendance = float(input("Enter your attendance: "))

if gpa >= 8.0:
    if attendance >= 75:
        print("Eligible for scholarship.")
else:
    print("Not eligible for scholarship.")
