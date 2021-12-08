# Given three integers, print the smallest one. (Three integers should be user input) 
a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
c = int(input("Enter third number:"))
if (a < b and a<c):
    print("the smallest number is {}:".format(a))
elif (b < a and b < c):
    print("the smallest numeber is {}".format(b))
else:
    print("the smallest number is {}".format(c))