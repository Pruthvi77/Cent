print("example2") # outputs example2 when the code is run
print(9) # outputs 9 when the code is run

print("word1 +" +  "word2 +" +      "word3") # outputs string "word1 word2 word3"
print("R" + str(2) + "-D" + str(77)) # outputs string “R2-D2”

#----------------------------------------

flat = "Falt Number G4"
Apartment = "Adike Anjani Homes"

print("My address is %s, Apartment name : --> %s" %(flat, Apartment) )
print("My address is %s, Apartment name : --> %s" , flat, Apartment , "\n" )# see the diffrene in console


#Updating String-------------------------------
var1 = 'Hello World!'
print("Updated String :- ", var1[:6] + 'Python')
print("updating first word",  'Updated '+ var1[6:])



#Input usage ---------------------------

Name = input("what is ur name ? --> ")
Place = input("Where do you live ? --> ")
Company = input("what is ur company name ? --> ")

print ("Ur Name is --> %s , U live in --> %s, U work for --> %s"%(Name,Place,Company))
