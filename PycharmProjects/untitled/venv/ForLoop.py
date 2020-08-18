string = "JambaLakadiPamba"

for i in string: #without range
    print(i)

for i in range(len(string)):  #with range
    print(string[i])


for i in range(len(string)):
    print(string[i], end=" ")
print(end="\n")



Dict = {"first":1 , "Second":2, "third":3}
for key in Dict:
    print(key + "--> " + str(Dict[key]))



string = "JambaLakadiPamba"

for i in string:
    print(i)

for i in range(len(string)):
    print(string[i])



#Zip dunction is used to execute mutiple lists simultaniuously
#Zipfunction --------------------------------------------------------------------------------------------
#Zip function list should be same length

list1 = [10,1,7.5,3]
list2 = [4,5,6,7]
i=0
for a,b in zip(list1,list2):

    if a>b:
        print("greater value at index %d is %d"%(i,a))
    elif b>a:
        print("greater value at index %d is %d"%(i ,b))
    i = i + 1

tuple= (1,2,3,4,5,6,7,8,9)
for i in tuple:
    if i < 5:
        print(i,end="")
    else:
        break
print ("\n")


#____________________________ if lists are not equal

list1 = [10,1,7.5,3]
list2 = [4,5,6]
i=0
for a,b in zip(list1,list2):

    if a>b:
        print("greater value at index %d is %d" % (i ,a))
    elif b>a:
        print("greater value at index %d is %d"%(i ,b))
    i = i + 1



    #####################3
list1 = [10,1,7.5,3]
list2 = [4,5,6,8]
i=0
new = []
for a,b in zip(list1,list2):
    z = a+b
    new.append(z)
    print(new)
else:
    print(12)


#------------------------------