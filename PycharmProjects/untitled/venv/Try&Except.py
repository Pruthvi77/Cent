ex = input("guess my favourite number")
try:
    if int(ex) == 7:
        print("wow, 7 is my favourite number")
    else:
        print("no luck, not my favourite number")
except:
    print("Please enter integer value only")
