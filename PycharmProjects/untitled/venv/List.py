List = ["ABC", "Pruthvi", "CH","Haha inserted"]
print(List)

Haha = List[1] + " " + List[2] + " <-- after appeding"
print(Haha)

List[0] = "SurName" #Reassigining the List element
print(List , "after reassignment")

List.append("My Name") # append elements to the list
print(List, "After appending ")

#Slicing the list same as strings
Slice1 =List[1:]

#index is used to know at which index firsttime element is apeared
Index = List.index("CH")
print(Index, " <-- CH Appeared at index %d in List" % Index)


#Inser is used to insert at any position in List not only at end
List.insert(1,"Haha inserted")
print(List, "After insertion at index 1")


#remove is used t remove a sngle item fromlist using exact value
List.remove("Haha inserted") #removes only first appeared element from  list
print(List,"After removal of an element \"Haha inserted\"")


#pop is used to remove item using index
List.pop(0) #Remove 0 index element
print(List,"after poping 0 index element")

List.pop() # Empty pop removes last element
print(List,"Removal happend for last element using pop() without index ")




#--------------------------------------------------------------

List1=["Me", "You", 12]
print(List1, "With different kind of data like int float string etc")

