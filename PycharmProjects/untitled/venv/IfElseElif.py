from setuptools import PackageFinder

if 5!= 6 :
    print("5 not equal to 6")
else :
    print("5 equals to 6")



# elif condition
if 5 == 6:
    print("5 equal to 6")
elif 5!=6: # between if & else ->n no. of elif's can be there
    print("\nelif condition: \n5 not equal to 6")
else:
    print("5 equals to 6")


import sys

ItemPrice = int(input("Enter the Price"))

if ItemPrice == 1:
    Price = 1.00
    print("it is water price", Price)
elif ItemPrice == 2:
    Price = 1.50
    print("it is cola price",Price)
elif ItemPrice == 3:
    Price = 2.00
    print("it is gatoride price", Price)
else:
    sys.exit("Please try again.")


quarters = int(input("Enter number of quarters"))
dimes    = int(input("Enter number of dimes"))
nickels  = int(input("Enter number of nickels"))
pennies  = int(input("Enter number of pennies"))


#Total =  (quarters * 0.25) + (dimes *0.10) + (nickels * 0.05 )+ (pennies *0.01)
Total =  quarters * 0.25 + dimes *0.10 +nickels * 0.05 + pennies *0.01
print("Total", Total)

if Total == Price:
    print("Ur bill is ", Total, "Have a nice day")
elif Total > Price:
    print("Take change ", Total - Price)
else:
    print("Need more", Price-Total)
