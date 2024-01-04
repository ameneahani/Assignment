print("Welcome to my BMI calculator")
w = float(input("Enter your weight (kg):"))
h = float(input("Enter your height(m) :"))

bmi = w / (h*h)
if bmi < 18.5:
    status="UNDERWEIGHT"
elif bmi >= 18.5 and bmi < 25:
    status="NORMAL"
elif bmi >= 25 and bmi < 30:
    status="OVERWEGHT"
elif bmi >= 30 and bmi < 35:
    status="OBESE"
elif bmi >= 35:
    status="EXTREMLY OBESE"
print("your fitness status is",status)