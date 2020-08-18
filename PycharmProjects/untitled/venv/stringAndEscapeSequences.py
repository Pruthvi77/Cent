var1 = 'Hello World!'
print ("Updated String :- ", var1[:6] + 'Bullshit')

var1 = 'Hello World!'
var2 = "Python Programming"

print ("var1[0]: ", var1[0])
print ("var2[1:5]: ", var2[1:5])
print ("var2[:2]: ", var2[:2])
print ("var2[2:]: ", var2[2:])


# we can assign empty string also as below
str = ""
print(str)

# type your code for "string and escape sequences"
lannisters = "JaimeCerseiTyrion"

Str = "This is how \" double quotes\" will be placed in a string"
print(Str)

Str = "This is how \' single quotes\' will be placed in a string"
print(Str)

# same as a = lannisters[1:2]
a = lannisters[1]
print(a)

# same as a = lannisters[0]
firtletter = lannisters[0:1]
print(firtletter)

# assign Jaime to a variable
FirstName = lannisters[:5]
print(FirstName)

# assign middle name to a variable "JaimeCerseiTyrion"
MiddleName = lannisters[5:11]
print(MiddleName)

# assign last name to a variable "JaimeCerseiTyrion"
LastName = lannisters[11:]
print(LastName)
print(lannisters[11:])     # we can also print directly like this without assigning
