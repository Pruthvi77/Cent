list = ["Me", "JilJil", "You", "Someone"]

x = list[0]+ " " +list[1]
print(x)


bust = [1 , 2, 3, 4]
x = bust[0]+bust[1]
print(x)


bust[0] = 0
x = bust[0]+bust[1]
print(x)

print(bust)

bust.append(5)# Append item to the last of the list
print(bust)  # after appending

index = bust.index(4) # 4 is present at index 3 it is search operation
print(index)


#Insert will be used to inserat item at any index
bust.insert(1,"Bum")
bust.insert(6,"Bum")
print(bust) # after inserting




#remove will be used to remove item at any index
bust.remove("Bum")
print(bust) # after removal of first appear on list

bust.pop() # removes the last element of the list
bust.pop(2) # removes the 2nd index element of the list
print(bust)