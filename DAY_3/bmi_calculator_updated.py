#BMI Calculator 2.0

hgt = float(input("Enter ur Height in cm : "))
wgt = float(input("Enter ur Weight in kg : "))

bmi = wgt / (hgt/100)**2

if(bmi < 18.5):
    print(f"U You are UNDERWEIGHT")
elif(bmi<25):
    print("You are NORMAL")
elif(bmi<30):
    print("You are OVERWEIGHT")
elif(bmi<35):
    print("You are OBESE")
else:
    print("You are CLINICALLY OBESE")