# Multiplication Operations [PEDMAS]

print(3*2+(5-2)**4/2-2%3)



# Round up the float
print(round(10/3,2))

# foramt
x = 100 / 3 
print("{:.2f}".format(x))



# f-strings

hgt = float(input("Enter ur Height in cm : "))
wgt = float(input("Enter ur Weight in kg : "))

bmi = wgt / (hgt/100)**2

print(f"Your Height is {hgt} cm , your Weight is {wgt} kg and you BMI is {round(bmi,1)}")




# Your Life left in days or weeks (rough calculation without leap days)

expected_yrs = int(input("Enter number of years u expect to live : "))
cuurent_age = int(input("Enter your current age : "))

years = expected_yrs - cuurent_age
months = years * 12
weeks = years * 52
days = years * 365

msg = f"You have {years} years or {months} months or {weeks} weeks or {days} days left"
print(msg)

