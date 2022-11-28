print("What is your name human?")
name=input()
print("How old are you?")
years=int(input())
height = float(input("How tall are you in cm?"))
weight = float(input("How much do you weigh in kg?:"))
BMI = weight / (height/100)**2
print(name,"you are",years,"and your bmi is",BMI)
