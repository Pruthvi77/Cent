#assignment 1 & Question 1
assignment= []
for i in range(2002,3200,7):
    if i % 5 ==0:
        continue
    assignment.append(i)
print(assignment)


#assignment 1 & Question 2
print("Enter First Name")
firstName=input()
print("Enter Second Name")
secondName=input()
Name=[firstName,secondName]
for i in Name:
     print(i[::-1])

#assignment 1 & Question 3
import math
    #this module was a google search
radius = 12
v = (4/3)* math.pi * radius**3
print("Volume of sphere is ", v, "cm_cube")
