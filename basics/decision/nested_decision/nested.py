print("What type of cover does the book have? select: soft/hard?")
cover = input()
if (cover == "soft"):
  print("Is the book a perfect bound? select: yes/no?")
  bound = input()
  if (bound == "yes"):
    print("Soft cover, perfect bound books are very popular!")
  else:
    print("Soft covers with coils or stitches are great for short books!")
else:
  print("Books with hard covers can be more expensive!")
