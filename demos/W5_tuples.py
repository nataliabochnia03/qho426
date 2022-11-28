def simple_tupels():
  person = ("Piotr", 67, False)

  #printing a tuple
  print(person)

  #check data type
  print(type(person))

  #Acces elements via index
  print(f"{person[0]} is {person[1]}years old")
  #No mutation possible!
  #person[0] = "Peter"
  #print(person)

  if person[2]:
    print("You have a doggo!")
  else:
    print("No doggo no fun!")

  #Tuples can be concatenated (joined) but this creates a different tuple
  p1 = person + (20, "none")
  print(p1)
  print(person)

  #min and max only works with number, no strings can be inside!
  t = (16, 8, 9, 21, 55)
  print(max(t))
  print(min(t))
  


simple_tupels()