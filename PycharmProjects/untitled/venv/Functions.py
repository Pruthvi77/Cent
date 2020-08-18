def flop():
    print("Bharath ane nenu is a flop")

flop()

#--------------------------------------------

def parameter(a):
    print(a)

parameter("jhgah")

#=============================================

def operations(a,b,c):
    d = b*c
    print(d + a)

operations(1,2,3)



#---------------------------
# Calling a function with in a function

def Function1(a,c):
    d= a+c
    print("Sum is",d)
    return d


def Funtion2(x,y):
    z= Function1(x,y)
    print("Value of z is", z,"when perform operation and assign it to a variable")

Funtion2(2,6)

#---------------------------------------------
def Function1(a,c):
    return a+c


def Funtion2(x,y):
    z= Function1(x,y)
    print("Value of z is", z, "when perform operation directly in return")

Funtion2(2,6)

#---------------------------------------------------------------------------------------
#call the function you created in step 3 with the variable you made in step 2 as its input

Five = 5

def referenc(ref):
    print(ref)

referenc(Five)



#-------------------------------------------
float1, float2, float3 = 1.2311, 3.26654, 8.254

def quote1(a,b):
    return a/b

def quote2(a,b,c):
    return quote1(a,b)/c

print(quote1(float1,float2))
print(quote2(float1,float2,float3))




#-------------------------------------------
float1, float2, float3 = 1.2311, 3.26654, 8.254

def quote1(a,b):
    return a/b

def quote2(a,b,c):
    return quote1(a,b)/c

print(quote1(float1,float2))
print(quote2(float1,float2,float3))



import  random # Importing a module

print(random.randint(1,777)) # prints randm value between 1 & 777

#-----------------------------------

from random import randint # we can aslo import sepcific function from module like this
print(randint(1,777)) # no need to mention module "random" here

#----------------------------------

#we caan import everyting from module like this

from random import*

print(random()) # print float number >0 and <1 (0-1)
# no need to mention module "random" here

x = random()*100
print("random float between 1 & 100 is ", x)


#----------------------------------

from math import *

y = sqrt(x)
print("sqrt of y is",y)

from sys import exit
exit(y)