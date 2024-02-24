# Tip Calculator

total = float(input("What is the total bill? : "))
tip = float(input("What percentage tip would you like to give? : "))
split = float(input("How many people to split the bill? : "))

total += total * (tip/100)
per_person = total / split
msg = f"Your total bill including tip is : ${round(total,2)} and split share per person is : ${round(per_person,2)}"
print(msg)