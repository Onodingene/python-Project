name = input("What is your name?")
intro = print(f"Welcome to your BMI calculator, {name}")
weight = input("What is your weight in kg")
height = input("What is your height in m")
bmi = float(weight)/(float(height) ** 2)
result = print(f"{name}, your BMI is {bmi}")

if bmi <= 18.5:
    print(f"{name}, you are underweight")
elif bmi > 18.5 and bmi < 25:
    print(f"{name}, you are normal weight")
else:
    print(f"{name}, you are overweight")
    
    
