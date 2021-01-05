#!/usr/bin/env python3

intro_msg = 'Given your weight in pounds and height in inches \nto find out which BMI category you are in\n'
    
result = ' '

bang = ', Come on, you need to start workout!'

print(intro_msg)

# force user to enter the desire input

while True:
    name = input("Hi there, I'm Jellyfish What's your name?\n").strip() 
    try:
        weight = int(input("Hi " + name + ", How much you weight in pounds?\n").strip())
        print("Input your height in Feet and Inches\n")
        h_ft = int(input("Feet: \n").strip())
        h_inch = int(input("Inches: \n").strip())
        break
    except:
        print("\...um...0_o...That's not right, let's try aagin")

# if all input value are satisfied then proceed 
# convert height in feet to inches
height = h_ft * 12 + h_inch
# formula to get BMI based on user input
BMI = round(703 * weight / (height * height))

if BMI < 15:
    result = 'Very severely underweight'
elif BMI >= 15 and BMI < 16:
    result = 'Severely underweight'
elif BMI >= 16 and BMI < 18.5: 
    result = 'Underweight'
elif BMI >= 18.5 and BMI < 25:
    result = 'Normal (healthy weight)'
elif BMI >= 25 and BMI <30:
    result = 'Overweight' + bang
elif BMI >= 30 and BMI < 35:
    result = 'Moderately obese' + bang
elif BMI >= 35 and BMI < 40:
    result = 'Severely obese' + bang
else: 
    result = 'Very severely obese' + bang  

print(result)
