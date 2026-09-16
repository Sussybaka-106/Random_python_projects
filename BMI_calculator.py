weight_kg = int(input("Enter your weight in kilograms:"))
height_meter = float(input("Enter your height in meter:"))

bmi_calculate = weight_kg / height_meter ** 2

print("Your BMI is:", bmi_calculate)