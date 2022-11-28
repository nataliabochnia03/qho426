
number1 = int(input("Please enter the first number"))
number2 = int(input("Please enter the second number"))
number3 = int(input("Please enter the third number")) 

even_numbers = 0
odd_numbers = 0 

if (number1 % 2 == 0):
    even_numbers = even_numbers + 1
else:
    odd_numbers = odd_numbers + 1

if (number2 % 2 == 0):
    even_numbers = even_numbers + 1
else:
    odd_numbers = odd_numbers + 1

if (number3 % 2 == 0):
    even_numbers = even_numbers + 1
else:
    odd_numbers = odd_numbers + 1
print("There is {} even numbers and {} odd numbers".format (even_numbers, odd_numbers))
