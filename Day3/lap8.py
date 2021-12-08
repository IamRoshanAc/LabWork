#given an n-digit number. Find the sum of its digits
number = 117
sum_of_digits = 0 
for digit in str(number):
    sum_of_digits += int (digit)
print(sum_of_digits)