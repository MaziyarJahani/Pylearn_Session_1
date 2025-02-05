# Write a program to get a weight (kg) and height (cm) of a person, calculates the BMI of person and classify it.

weight = float(input("Enter weight (kg): "))
height = float(input("Enter height (cm): "))

height_in_meters = height / 100

bmi = weight / (height_in_meters ** 2)

if bmi < 18.5:
    classification = "Underweight"
elif 18.5 <= bmi < 24.9:
    classification = "Normal weight"
elif 25 <= bmi < 29.9:
    classification = "Overweight"
elif 30 <= bmi < 34.9:
    classification = "Obesity"
elif 35 <= bmi :
    classification = "Extreme Obesity"

bmi_rounded = round(bmi, 2)

print("Your BMI is", bmi_rounded , "which is classified as: ", classification)