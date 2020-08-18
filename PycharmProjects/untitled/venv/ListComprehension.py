ex = [items for items in range(0,10000,2)]
print(ex)

ex = [items for items in range(1,10000,2)]
print(ex )

ex1= [num for num in range(10)]
print(ex1)

ex2= [num*3 for num in range(10,20)]
print(ex2)

ex3= [num for num in range(10,20,2)]
print(ex3)

#--------- using if in For loop

ex4= [num for num in range(10) if num%2==0]
print(ex4)

ex5= [num for num in range(12) if num%2==0 and num % 5==0]
print(ex5)

ex6= [num for num in range(10) if num > 3]
print(ex6)


print([a for a in range(10, -1, -2)])



#-------------------Slicing list
list1 = [0,1,2,3,4,5,6,7,8,9]
print(list1[0:10:3])

print(list1[::2])
print(list1[8:1:-2])
print(list1[::-1]) #to revrese a string
