#Write a program to calculate the BMI of a person?

height=float(input("Enter your height in meters: "))
weight=float(input("Enter your weight in kilograms:"))
BMI=weight/(height*height)
print("Your BMI is:",BMI)
if BMI <= 18.4:
    print("You are underweight")
elif 18.4 <=  BMI <=  24.9:
    print("You are healthy")