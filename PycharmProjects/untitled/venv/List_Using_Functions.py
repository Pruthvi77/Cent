List = ["Very", "Good", 31, "Morning"]

def Wish(li):
    return li

print(Wish(List), "<-- passing list t a function") # Passing a list values to function
print(Wish([1,2,3]))

#Accessing list value sng function
def access(li):
    return li[2]

print(access(List), "<-- list element using function")


#moditing lis value using funtion
def Modify(li):
    return li[2]/2
print(Modify(List))

#Manupulate list using function
def manupulate(li):
    li.remove("Morning")
    li.append("Afternoon")
    return li
print(manupulate(List), "<-- list after manupulating")