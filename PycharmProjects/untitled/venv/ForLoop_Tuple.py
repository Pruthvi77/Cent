# Tuple will be in () where as list wll be []
Tuple = (12, "March","Friday")
print(Tuple)

# Tuple will be in () where as list wll be []
Tuple = (12, "March","Friday", True, 5.647)
print(Tuple)

Tuple2 = 5.6, "Hi", "Abbooo" , "Oohhooo"# Tuple can also be declared like this
print(Tuple2)


EmptyTuple = () #  This is an empty tuple
print("Empty Tuple will be like this ", EmptyTuple ,end = "\n\n")


# Accessing tuple vlaue & slicing  is same as LIST
print("2nd value of the Tuple 1 is -->" ,Tuple[1])
print("Slicing iif Tuple2 -->" , Tuple2[1:], end = "\n\n")




# For loops ---------------------------------------
for elements in Tuple:
    print(elements)


ListOne = [1,2,3,4,5,6,7,8,9,10]
Empty = []

Tuple = ("My", " Name", " Is ", "Jigalle")
song =""

for i in ListOne:
    if i > 2 and i<8: # append only elemnts between 2-8
        Empty.append(2.5*i)
print("Empy list after appendig", Empty, end = "\n\n")


for i in Tuple:
    song+= i
print("tuple after concatinating", song)



# Example -------------------------------------------
