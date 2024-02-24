#BMI Calculator

hgt = float(input("Enter ur Height in cm : "))
wgt = float(input("Enter ur Weight in kg : "))

bmi = wgt / (hgt/100)**2

print("Your BMI is : " + str(int(bmi)))