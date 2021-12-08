import math
realNumber = float(input("Enter a real number"))
a, b = math.modf(realNumber)
print(b)