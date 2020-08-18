# we will use  len() method to get the length of any string
String = "BumChickBum"
LentgthOfString = len(String) # assigns the number of characters in the string "BumChickBum" to the variable LentgthOfString
print(LentgthOfString, "Lenth of the string") # prints the number of characters in the string "BumChickBum", which is 11

#---------------------------------------------------

# we will use the str() method to convert any variable to string
Number1 = 9
CovertedNumber1 = str(Number1)

Number2 = 9.123
CovertedNumber2 = str(Number2)
print(CovertedNumber1,"\"Coverted string 9\"    & " ,CovertedNumber2, "\"Coverted string 9.123\"")




# -----------------------------------------------------

""" .lower() method to make all the characters in a string lower case
    .upper() method to make all the characters in a string upper case"""

str1 =  "LOWER"
str2 =  "lower"
string  =  "LoWeR"
print(str1.lower(),"\" Conver LOWER to lower\" \n",str2.lower(),"\"Conver lower to lower\" \n",
      string.lower(),"\"Conver LoWeR to lower\" \n")

str3 = "upper"
str4 = "UPPER"
string  = "uPpEr"
print(str3.upper(), str4.upper(), string.upper())

#---------------------------------------------------- Exercise

print(len("JilJil"))
print(str(123)[1]) # conver number to string here itself and print second letter of it
print("JILJIL".lower())
print("paapA".upper())


Number = 19.125
print(str(Number)[2],"--> 3rd element of converted srtirng 19.125") #It will print "." dot as it is 3rd element of the string

sliceLen = len(String[1:4]) # String = "BumChickBum"
print(sliceLen)



sliceLen = len(str(Number2)[1:5]) # Number2 = 9.123
print(sliceLen, "Length of [1:5] of converted string --> Number2 = 9.123")


# ------------------------# Take cares of capitalisation of a line
str = "tHIS is STRING cAPITAL example. what can i do with this "
print ("str.capitalize() : ", str.capitalize())  # Prints --> This is string capital example. what can i do with this


#-----------------------
str = "tHIS is STRING cAPITAL example. what can i do with this !";
print(str.swapcase()) # Prints --> This IS string Capital EXAMPLE. WHAT CAN I DO WITH THIS !

