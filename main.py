#Write a program to check whether the given values have boolean values or not.

a=5
b=5
c=5


if (a and b and c==1)  or (not a and not b and not c) :
    print("All are boolean")
elif a or b or c :
    print("At least one is boolean")
else:
    print("None are boolean")  
if (a,b,c>0):
    print("All are boolean")
else:
    print("At least one is boolean")    