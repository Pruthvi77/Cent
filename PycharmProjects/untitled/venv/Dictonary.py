#dectionalry = {Key1:"Value1",Key2 : "Value2,Key3 : "Value3"}
Dection = {1:"I", 2 : "am", 34: "Pruthvi"}
print(Dection)  #Dic key can be num, strg ....anything

print("key 34 value is -->", Dection[34]) # Dectionary[Key] to access the value in Key

EmptyDectionary = {} #EmptyDictionary

#-------- Add new key & value to dectionary
EmptyDectionary[30] =  "New1"
EmptyDectionary[21] =  "New2"

#------------ length of dictonary is len(Dict)
print(len(EmptyDectionary), "<-- Leght of dictopnary using len()", end="\n\n")


#----------- Reassigning a value to the key of dectionay will be

print("Before reassigning the Dectionary", EmptyDectionary)
EmptyDectionary [21] =  "Reassigned"
print("After reassiging", EmptyDectionary)


#Remove a Key& Value from Dectionalry using del
del EmptyDectionary[21]
print("After removing the key 21 from dectionaty", EmptyDectionary)