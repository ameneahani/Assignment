
name = input("Please enter your fist name: ")
family = input("Please enter your last name: ")
grade1 = float(input("Please enter the grade of the first lesson: "))
grade2 = float(input("Please enter the grade of the second lesson: "))
grade3 = float(input("Please enter the grade of the third lesson :"))
ave = grade1 + grade2 + grade3
if ave >= 17 :
    status = "Grate"
elif ave >= 12 and ave<17:
    status = "Normal"
else :
    status = "Fail"
print("Dear", name , family , "your status is", status)
