
height = float(input("Please enter the height :"))
weight = float(input("Please enter the weight :"))
BMI = weight /(height*height)
if BMI < 18.5:
    sta ="Under Weight"
elif 18.5 <BMI<24.9 :
    sta ="NOrmal Weight"
elif 25 <BMI< 29.9 :
    sta ="Over Weight"
elif 30 <BMI< 34.9 :
    sta ="Obesity"
else :
    sta = "Extra Obesity"
print("your status is", sta)






