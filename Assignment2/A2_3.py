# calculate average of student's scores
number_of_score = 0
sum = 0
while True :
    student_score = input("enter your score or type exit: ")
    number_of_score = number_of_score +1
    if student_score == "exit":
        average = sum/ number_of_score
        print ("Your average is: ", average)
        break
    student_score = float(student_score)
    sum = sum + student_score

