print("Program started!.")
asc = int(input("Please enter an ASCII code: "))
if (asc >= 32 and asc <= 126):
  print("The character represented by the ASCII code ",asc, "is: ",chr(asc))
else: 
  print("The character cannot be displayed.")
print("Program ended!")

