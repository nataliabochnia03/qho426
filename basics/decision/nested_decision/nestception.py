print("Where should I look?")

look1 = input()
if (look1 == "In the bedroom"):
  print("Where should I look in the bedroom?")
  look2 = input()
  if (look2 == "under the bed"):
    print("found some shoes but no battery")
  else:
    print("found some mess but no battery")


elif (look1 == "In the bathroom"):
  print("where in the bathroom should I look?")
  look3 = input()
  if (look3 == "under the sink"):
    print("Found a robber duck but no battery")
  else:
    print("Found a wet surface but no battery")
    
elif (look1 == "In the lab"):
  print("Where in the lab should I look?")
  look4 = input()
  if (look4 == "on the table"):
    print("Yes! I found my battery!")
  else:
      print("Found some tools but no battery.")
else:
  print("I don't know where that is but I will keep looking")
  


