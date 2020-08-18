"""
# List of priority
1 not
2 and
3 or
"""

# AND operator
ex1 = True and True # ex1 = True
ex2 = True and False # ex2 = False
ex3 = False and True # ex3 = False
ex4 = False and False # ex4 = False
print("True and True --> "  , ex1)
print("True and False --> ", ex2)
print("False and True --> ", ex3)
print("False or False --> ", ex4, "\n\n")



# OR operators

ex1 = True or True # ex1 = True
ex2 = True or False # ex2 = True
ex3 = False or True # ex3 = True
ex4 = False or False # ex4 = False
print("True or True --> "  , ex1)
print("True or False --> ", ex2)
print("False and True --> ", ex3)
print("False or False --> ", ex4, "\n\n")


# Not operation

ex1 = not True # ex1 = False
ex2 = not False # ex2 = True
print("not True --> "  , ex1)
print("not False --> ", ex2)


#--------------- Expressiosn
ex9 = not False and not True or False # not will execute first and give step1
step1 = True and False or False # and will execute 2nd and five step2
step2 = False or False # or will execute 3rd and give result
result = False
print("ex9= not False and not True or False  --> ", ex9)


#----------------------------------

notEqualToTru = 8>5 and 2*2 < 3*3
print(notEqualToTru)

"""
order of operations for Boolean operators:
1.make var1 evaluate to False by changing or removing a single Boolean operator 
2.make var2 evaluate to True by changing or removing a single Boolean operator
"""


var1 = not 3>1 and 5 != 2 or 6 != 6   # var1 = ​not ​3 ​> ​1 ​and ​5 ​!= ​2 ​or ​6 ​== ​6
var2 = 4*2 !=6 or not 2%6 == 1       # var2 = ​4 ​* ​2 ​!= ​6 ​and not ​7 ​% ​6 ​== ​1
print("var1 %s \nvar2 %s"%(var1, var2))


#print("var1 %s \nvar2 %s"%(var1,var2)




# type your code for "and, or, and not" below this comment and above the one below it. ------------------
# 1. and1 = True and True
and1 = 5>=5 and 7 <8

# 2. and2 = False and True
and2 = False and 8 != 1

# 3. or1 = False or True
or1 = 7* 7 == 48 or 7 **2 != 48

# 5. not1 = not False
not1 = not 7 ==10

# 6. not2 = not True
not2 = not 5<=5
print("and1 = %s \nand2 = %s\nor1  = %s \nnot1 = %s\nnot2 = %s"%(and1, and2, or1, not1,not2))