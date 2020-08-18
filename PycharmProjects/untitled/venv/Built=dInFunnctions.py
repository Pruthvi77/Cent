x = abs(-97)
y = abs(88.214)
z = abs(87/-54)
print("x = %s, y= %s, z = %s "%(x,y,z))



# Type function
x = type(123)
y = type(21.321)
z = type(214/-45)
t = type("dfvbdds")
s = type(True)

print("x=%s, y= %s, z=%s, t=%s, s=%s"%(x,y,z,t,s))

print(type(123),"<-- this is 123 type")


#-----------------------------------------------------------

li = [1, 9, 8, 4]
print("Multiply elements of li with 2  -->",[elem*2 for elem in li]) #Multiply elements of list with 2
print(li)
li = [elem*2 for elem in li]
print(li)


#---------------------------------------
#





params = {"server":"mpilgrim", "database":"master", "uid":"sa", "pwd":"secret"}    # Remember it ****************
#The keys, values, and items Functions
print(params.keys()) #['server', 'uid', 'database', 'pwd']
print(params.values()) #['mpilgrim', 'sa', 'master', 'secret']
print(params.items())  #[('server', 'mpilgrim'), ('uid', 'sa'), ('database', 'master'), ('pwd', 'secret')]




#--------------------------------------------------------------
# max function
ex1 = max(12,245,12.221,78.2114)
print(ex1)
print(max("as","sd","sw","ss"))

# min function
ex1 = min(12,245,12.221,78.2114)
print(ex1)
print(min("as","sd","sw","ss"))

#--------------------------------------------------------------

ex1 = max(12,245,12.221,78.2114)
print(ex1)
print(max("as","sd","sw","ss"))


ex1 = min(12.22,245,12.221,78.2114)
print(ex1)
print(min("as","sd","sw","ss"))





#------------------------------------------------------------------------



