name = input("Enter your name: ")
height = float(input("Enter your height(m): "))
weight = float(input("Enter your weight(kg): "))
BMI = round(weight / (height*height),2)
print("Hi",name,"Your BMI is",BMI)
