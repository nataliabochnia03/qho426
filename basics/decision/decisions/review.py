

drink = input("What should I drink?: ")
if ((drink == "coffee") or (drink == "tea")):
  add = input("Shuld I add something to it?")
  if (add != "vodka"):
    print("I want somenthing stronger!")
  else:
    print("Good choice!")
elif ((drink == "rum") or (drink == "cocktail")):
  print("Great choice!")
else: 
  print("I am not a big fan of this drink!")
