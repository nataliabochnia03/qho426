print("Program started!")
print("Please enter a standard character:")
letter = input()
if len(letter) == 1:
  value = ord(letter)
  print(f"The ASCII code for {letter} is {value}.")
else:
  print("Wrong input given.")
  
print("Program ended")