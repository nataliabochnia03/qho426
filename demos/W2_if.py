name = input("Enter your name: ")

if len(name) > 8:

  print("You have a loooong name! Can I use a nickname please?")
elif len(name) <= 3:
  print("Wooow, your name is super short, and easy to remember")
elif name == "Piotr":
  print("That's a boring name!")


else:
  print("Oh,your name is pretty short!")
print("Nevertheless, welcome to the session! {}!".format(name))
