def reverse(string):
  reversed_string = ""
  for i in string:
    reversed_string = i + reversed_string
  print("Reversing...")
  print("The phrase is...:", reversed_string)
string = input("What phrase do you see?: ")
reverse(string)

