#Initialise empty set
s = set()

#Check the type is set
print(type(s))

#Initialise non-empty set
colours = {"blue", "red", "purple", "green"}

print(colours)

#Adding elements to a set
colours.add("Black")
colours.add("turquoise")

print(colours)

#Delete an element of a set
colours.remove("blue")

#Check membership
if "blue" not in colours:
  print("Yeah my favourite colour is here!")
else:
  print("You are missing an important colour")

colors = {"yellow", "black", "red", "cyan"}

#Take union of two sets -join them together but do not keep duplicates
print(colours.union(colors))

#take intercetion of two sets which is a "common" elemnets 
print(colours.intersection(colors))

#Take set difference - so only keep elements NOT in another collection
print(colours.difference(colors))