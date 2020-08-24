#1
try:
    val = 5/0
except :
    print("Error : incorrect mathmatical expression")


#2
subjects=["Americans ","Indians "]
verbs=["play ","watch "]
objects=["Baseball","Cricket"]
FinalList = [sub+ ver+ obj for sub in subjects for ver in verbs for obj in objects]
for item in FinalList:
    print(item)
