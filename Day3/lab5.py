#For given integer x, print ‘True’ if it is positive, print ‘False’ if it is negative and print ‘zero’ if it is 0. 
x = int(input("enter a number:"))
if (x > 0 ):
    print(f"it is positive")
elif (x < 0):
    print(f"it is negative")
else:
    print(f"it is zero")