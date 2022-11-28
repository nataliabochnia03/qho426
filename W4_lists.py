#Declare empty list
hated = []

#declate non-empty list
fav = ["Carbonara", "Pizza", "Casatiello", "Pierogi"]
#print full list
print(fav)


#print a single element
print(fav[2])

#Add elements at the end of the list
hated.append("Tofu")
hated.append("Beans")
fav.append("Lasagne")

#appending using a loop and user input
for i in range(2):
  print("Enter another hated dish: ")
  dish = input()
  hated.append(dish)

#print out the lenght/size of my list "hated"
print(len(hated))

#insert data at any position on the list 
print(fav)
dish = input("Enter next dish to be inserted to be 1st position: ")
fav.insert(1,dish)
print(f"The number of favourite dishes is: {len(fav)}")
print(fav)
fav.insert(3, "pancakes")
print(fav)
print(f"The number of favourite dishes is: {len(fav)}")

#remove item from the list 
fav.remove("Casatiello")



print(fav)

#remove by index (and return)
x = fav.pop(1)

#delete an item via index (forever and ever!)
del fav[2]


print(fav)

#slicing
print(hated[::-1])

#finding in what position is something located:
for i in range(len(fav)):
  if fav[i] == "Pizza":
    print(f"Pizza is located in position {i} ")
    