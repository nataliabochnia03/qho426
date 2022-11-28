#powtorzyc przed testem w razie czego, bo nie do konca rozumiem i mialam wiecej szczecia niz rozumu piszac ten kod!!


print("Please enter a number: ")
number = int(input())
#Factorial is a non-negative integer. It is the product of all positive integers less than or equal to that number you ask for factorial. It is denoted by an exclamation sign (!). 
# Example:
# n! = n* (n-1) * (n-2) *........1  
#factorical=silnia
factorical = 1
while (number > 0):
  factorical = factorical * number
  number = number - 1
print("The factorical is: ", factorical)
