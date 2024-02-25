# Conditional Loops  if/elif/else

#Odd or Even
num = int(input("Enter the number : "))
if(num == 0):
    print("It's neither Odd or Even")
elif(num % 2 == 0):
    print("It's Even")
else:
    print("It's Odd")



#Multiple if 
    
#Automatic Pizza Order Program

size = input("Welcome to Py Pizza!!! \n What size of pizza would u like? S, M or L : ")

if(size == "S"):
    price += 15
elif(size == "M"):
    price += 20
elif(size == "L"):
    price += 25
add_pep = input("Do you need pepperoni? Y or N \n")
if(add_pep == 'Y'):
    if(size == "S"):
        price += 2
    else:
        price +=3

cheese = input("Do you need Cheese? Y or N \n")
if(cheese == 'Y'):
    if(size == "S"):
        price += 1
    else:
        price +=2
print(f"Your total bill is : $ {price}")
