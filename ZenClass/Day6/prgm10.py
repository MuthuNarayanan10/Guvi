number = int(input("Please Enter any Number: "))

first_digit =last_digit = number
 
while (first_digit >= 10):
    first_digit = first_digit // 10
    last_digit = number % 10

print("The First Digit from a Given Number {0} = {1}".format(number, first_digit))
print("The First Digit from a Given Number {0} = {1}".format(number, last_digit))