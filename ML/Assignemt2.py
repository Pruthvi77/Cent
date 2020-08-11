for i in range(1,6):
    for j in range(i):
        print('*', end=" ")
    print(" ")

for i in range(6,0,-1):
    for j in range(i):
        print('*',end=" ")
    print(" ")

strng = input("Enter a string here, I will reverse it for you :")
print(strng[::-1])

