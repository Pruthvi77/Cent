from functools import reduce



"""
print("1) hellow world")
i=10
type(i)
	#to get whether i  is int, float, char, string...etc

i = "string"
	# “” for string

x = list()
# to declare an empty list

x= 1+6j
print("2) type of variable is ", type(x))
	# a real number & an imaginary number
	#then python will understand it is a complex variable

print("3) imaginary part is ",x.imag)
    #to get imaginary part

print("4) real part is ", x.real)
    #to get real part

print("5) address of the variable 'x' is" , id(x))
    #to get address of the variable

print("6)", True + True)
    # 1+1 = 2

concatinate = "Joining"+"W  ords"
print("7) This is a concatinated word",concatinate)

print("8) conveting integer to string " , str(1) + " 1 is string now")


x = (1, 2, 3, 4, 5, 6,7)
	# defining a tuple, it is a non editable.
	# Accessing the tuple data elements is same like list
x = [1, 2, 3, 4, 5, 6,7]
	# defining a list

#For loop
for number in x :
	if(number % 2 ==0):
		#  % will give reminder
		# == is to compare
		# if number%2 is 0: also same like above
		print(number, "is even")
	else:
		print(number, "is odd")

print(x[-2:])	#This is to print the last 2 elements of the list

x.extend([7,8])
	#This is to append multiple values to the list

x.append(9)
	#This is to append a single value to list

print(x.sort())
	#This will sort the values

x.sort(reverse=True)
	#This will sort the values in reverse order
	## We can pass parameters in functions

y = x.copy()
	#This will shallow copy x into y
	# shallow copy : use the same reference. Here changes in one element will reflect in other

print("9) Please enter something here ")
io = input()
    #input is to take input from keyboard
print("Entered input is -->",io)

m = ['Pruthvi','Raj']
    #mutiple values list should be like this

m = list("Pruthvi")
print("10) list is split like this ", m)

print("11) to print the list in reverse order", m[::-1])
m.append("Ch")
    #to append itemm to tail of the list
print("12) appended list is ", m)

m.insert(7,['Raj'])
    #to insert in middle of a list
print("13) after inserting 'Raj' in middle",m)

Raj = list(m[7][0])
print("14) splitting a list inside a list",Raj)
    #Parsing: means extracting data




############to revere a list and aso dataset inside list
z = []
for i in [1,2,3,"my",["name","is","Pruthvi"]]:
    if type(i) == list:
        for x in i[::-1]:
            z.append(x[::-1])

print("to revere a list and aso dataset inside list --> ",z)



##############for loop usig 'range'
for i in range(1,10,2): # 1-100 and 'i' increment by 2
    print(i)

########## fro loop with else
for i in range(1,10,2):
    print(i)
else:
    print("For-else-> no item left")

######### while loop
i =0
n = 10
sum = 0
while i < n:
    sum = sum+i
    i = i+1
print("sum of i using while loop",sum)

########## Range
x = list(range(10))
    #this will generate values from 0-9 and takes 1/2/3 arguments
print("Values based on range (10)",x)

########## Range high to low
x = list(range(10,0,-1))
    #if we dont give -1, it will try to get 11,12,13..which are not there
print("Values based on range (10) in reverse order",x)

#########break & Continue
# break will break the execution of whole loop
# continue will skipp one step in loop

for i in "string":
    if i == "i":
        continue
    print(i)
print("continue in 'for' loop skipped 'i' above")



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


s = "HelloWorld"
    #this 's' will be treated as tuple not list . So it is immutable
x= s.center(20,'z')
print("using s.centre function to add z on corners --> ",x)
        # to fill data in coreners with Z and make it 20 in total

print("is s is alphanumeric -->",s.isalnum())
print("is s is alphabetic -->",s.isalpha())
print("is data set is ending with 'd' -->",s.endswith('d'))
print("using split function with 'W' and it is list  --> ",s.split('W'))
print("using partitions function with 'W' and it is tuple with first occurance of 'W' --> ",s.partition('W'))
    #non primitive data : is like list, tuple...

data = [0,11, 'hi', 'how', 'are', 'you']
print("My Data is ",data)
data.pop()
    #data.pop(2) is to remove from an index
print("Pop: removing elemnets from list perminantly based on index +-> ", data )
data.remove('hi')
    #we use reomve to remove based on value
print("Pop: removing elemnets from list perminantly based on value +-> ", data )

data = [2,4,5,7,8,54,64,4,6]
data.sort()
print("sorting my list - > ", data)



# Let's make three lists
lst_1=[1,2,3]
lst_2=[4,5,6]
lst_3=[7,8,9]

# Make a list of lists to form a matrix
matrix = [lst_1,lst_2,lst_3]
print("get a element datt from list of list __>",matrix[2][1])

# Build a list comprehension by deconstructing a for loop with in a []
first_col = [row[0]**2 for row in matrix]
print("squre of 1st element of each list __> ",first_col)
l = [i for a in matrix for i in a]
print("list comprehension ",l)



############ tuple #####################
t = (1,2,5,True,'hey', 'ur','awsome')
print("Type of t s -->", type(t))
print(t)
    #we can't change/modify tuple
    #But we can change the ist values which are there inide tuple
t = (1,2,5,True,'hey', 'ur','awsome', ['am','also', 'awsome'],('why', 'not', 'me'))
print("Tuple can hold list & tuples inside it -->",t)
    #we need tuple only when we dont wnat anyone to manupulate like password

l = list(t)
        #getiing tule values into a new list , then we can modify list values
print("Tuple converted into list ->",l)

print("list converted as tuple -->",tuple(l))
    # we can convert list also into tuple


x = set("pruthvi")
    #this will take only 1 argument & iteratable thigs
    #it will remev al duplicates and print only 1 element & display in order
print("String using 'set'",x)

x = set([1,2,2,2,4,5,6,6,6,6,7,8,8,8,55])
print("removing duplicate using 'set'",x)

dict = {'key1':'Hi','key2':'how','key3':'300'}
print("Our dictionary is -->",dict)
print("getting a value of dictionary using key -->",dict['key2'])
    #we can keep a adictonary inside ditnary as below
    #nested dictinoary is possible

dict2 = {'key1':'Hi','key2':'how','key3':'300','key4':{'item':'apples','key4':'price','key5':1500 }}
print("dict inside a dict ->",dict2)
print("accessing a dict insie dict values -->",dict2['key4']['item'])
dict2['extreKey'] = "rupees"
print("dict2 after adding a new key",dict2)
print("Gettig only keys of dict --> ", dict2.keys())
print("Gettig only values of dict --> ", dict2.values())




###### function ###########
def sum(num):
    return num**2 , num
    #we can return N number of values in pythin


############ iterator #############
lst = [0,1,2,3,4,5,6]
lst1 = lst.__iter__()
    #this __iter__ will iteraate through the list & we access one by one lement as shown below
print("1st element of loop",next(lst1))
print("2nd element of loop",next(lst1))
print("3rd element of loop",next(lst1))
    #next will take you to next index of list, till last index f the list

############### generator #############
def squre(num):
    squre_list=[]
    for i in num:
        squre_list.append(i*i)
    return squre_list
print("Squered list using loop is -->",squre(lst))


def squre_generator(num):
    for i in num:
        yield i*i
            #'yield' always through the generted data insteda of loading a big billion list at once whicl occupy whole RAM memory
lst2=squre_generator(lst)
print("list after using generator",lst2)
print("Squered list using generator is -->",squre_generator(lst2))
print("1st element of loop",next(lst2))
print("2nd element of loop",next(lst2))
print("3rd element of loop",next(lst2))
    #next will take you to next index of list, till last index f the list


def half(a):
    return a / 2
lst = [1,2,3,4,5,6]
x = list(map(half,lst))
    #basicaly function will run using only 1 parameter, 'MAP' will help to iterate a list with function
print("iterate through all elements of a list to a functon -> ",x)


 #### posistion argument & keyword argumnet #########
# here 'name' is 'positional' arguments which we need to pass
# 'age' is the 'keyword' argument which already has defined value

def greeting(name,age=27):
    print("my name is '{}' and my age is {}".format(name,age))

greeting('pruthvi')

def squre(i):
    return i*i

print("using squre function ->", squre(5))
f = lambda i:i*i
    #lamnda function we can give only 1 expression
print("Using 'Lambda' function ->",f(5))

from functools import reduce
lst = [1,2,3,4,5,6,]
sum = reduce(lambda x,y:x+y,lst)
    #reduce is used when sum involved , with in one line of code
print("sum of a list using reduce -->",sum)

sum = filter(lambda x:x%2==0,lst)
    #filter is used when have one condition to check
    #whenever the resulte is true, it will prn that vaue
print("even numbers of a list using reduce -->",list(sum))


#define a class as below

class car:
    pass


#creating an object of class
bmw = car()

bmw.wheel = 4
bmw.breaks = True

print("wheel of car BMW is-->",bmw.wheel)





########## assiignment 3 ############
lst = [1,2,3,4,5,6,]
def myreduce(values):
    sum = 0
    for i in values:
        sum = i + sum
    return sum
print("Sum of list of values [1,2,3,4,5,6] using custom reduce 'function' -->",myreduce(lst))

def myfilter(list_values):
    empty_list = []
    for i in list_values:
        if i%2 ==0:
            empty_list.append(i)
    return  empty_list

print("getting even numbers just like 'filter' in [1,2,3,4,5,6] using custom function -->", myfilter(lst))


input_list = ['x','y','z']
list1 = [i*num for i in input_list for num in range(1,5) ]
print(list1)

list2 = [i*num for num in range(1,5) for i in input_list ]
print(list2)

list3 = [ [i+num] for i in range(2,5) for num in range(0,3) ]
print(list3)

list4 = [ [item+num for item in range(2,6)] for num in range(0,4)  ]
print(list4)

list_append = [list3,list4]
print("final list -> ",list_append)


list5 = [(num,i) for i in range(1,4) for num in range (1,4) ]
print(list5)


########## assignment 4 #######################
class area_triangle:
    def __init__(self, a, b, c):
        self.a = float(a)
        self.b = float(b)
        self.c = float(c)

    def calculate_area(self):
        s = (self.a + self.b + self.c) / 2
        self.area = float((s * (s - self.a) * (s - self.b) * (s - self.c))) ** 0.5
        return self.area

a, b, c = input("a = "), input("b = "), input("c = ")

t = area_triangle(a, b, c)
print("area : {}".format(t.calculate_area()))


def filter_list(input_list, number):
    return (x for x in input_list if len(x) > number)

list1 = input("Enter some words here as input with comma(,) seperate: ")
number = input("Enter number to filter based on length of words: ")
n = int(number)
list_split = list1.split(",")

print(list(filter_list(list_split ,n)))



list_words = ['one','two','three','four','five','six','seven']
list_count = [len(i) for i in list_words]
print("Length of each word in a list -->",list_count)



def is_vowel(char):
    vowels = 'aeiou'
    return char in vowels

print("Is 'c' is a vowel -->",is_vowel('c'))
print("Is 'e' is a vowel -->",is_vowel('e'))




#print below format
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *


############ Assignment 2 ##################
for i in range(1,6):
    for j in range(i):
        print('*', end=" ")
    print(" ")

for i in range(6,0,-1):
    for j in range(i):
        print('*',end=" ")
    print(" ")

strng = input("Enter a string here, I will reverse it for you :")
print(strng[::-1])





###############Classes ###############

class human:
    pass

pruthvi = human()
pruthvi.sername = 'Cherupally'
pruthvi.height = 5.8
pruthvi.wife='Nithya'
print("Printing class values using OOPs -->", pruthvi.sername, pruthvi.wife, pruthvi.height)


class person:
    def __init__(self, name, dob, height, wife,age):
        # __init__ is inbuld function to intialize variables
        #self is like a pointer,
        self._name = name
            #whenever a variable starts with '_', that means it is a protected variable
        self.dob = dob
        self.__height = height
            #whenever we usser double underscore '__', that means it is a private variable
        self.wife = wife
        #we can keep or name also instead of self, whever kept as first will be treated as pointer not variable

    def __str__(self):
        return "%s height is %s and wife name is %s" % (self._name, self.__height,self.wife)
        #'__str__' is used to return string instead of hexadecimal code

me = person('pruthvi',1994,5.8,'Nithya',27)
print(me)


######## inheritance ###############
#is like getting all paraent class properties in chile classs
#getting person class properties into child class like below
class child(person):
    def __init__(self, child_ID, *args):
        super(child, self).__init__(*args)
            # super is used to initilise everything from 'person' class
        self._child_ID = child_ID
            # child_ID is a local variable
            # '*args' is used to bring all parent class variables into child class

pruthvi = child('11e11a0424','pruthvi',1994,5.8,'Nithya',27)
    #here only child id is from child class, remaining are taken from 'person' class

print("getting name using inheritancce -->",pruthvi.wife)


######### encapsulation############
# calling all classes inside a class
class Tyres:
    def __init__(self, branch, belted_bias, opt_pressure):
        self.branch = branch
        self.belted_bias = belted_bias
        self.opt_pressure = opt_pressure

    def __str__(self):
        return ("Tyres: \n \tBranch: " + self.branch +
                "\n \tBelted-bias: " + str(self.belted_bias) +
                "\n \tOptimal pressure: " + str(self.opt_pressure))


class Engine:
    def __init__(self, fuel_type, noise_level):
        self.fuel_type = fuel_type
        self.noise_level = noise_level

    def __str__(self):
        return ("Engine: \n \tFuel type: " + self.fuel_type +
                "\n \tNoise level:" + str(self.noise_level))


class Body:
    def __init__(self, size):
        self.size = size

    def __str__(self):
        return "Body:\n \tSize: " + self.size


class Car:
    def __init__(self, tyres, engine, body):
        self.tyres = tyres
        self.engine = engine
        self.body = body

    def __str__(self):
        return str(self.tyres) + "\n" + str(self.engine) + "\n" + str(self.body)


t = Tyres('Pirelli', True, 2.0)
e = Engine('Diesel', 3)
b = Body('Medium')
c = Car(t, e, b)
print(c)


###########################################

# myfile = open('Resources/debug.txt')
    #to open a file and store in a available
#myfile.read()  #to read file line by line
#myfile=open('path', 'a+') #this will be used to open the fie in append mode
# for line in open('file_path')
    #print(line) #to read all line of data of a file
#myfile.write("this text will appened to my file")

"""


################ exceptional handling ##############
myfile = open('Resources\debug.txt')
try:
    myfile = open('Resources/debug.txt')
    print("file has loaded sucessfully")
    pass
except:
    pass
