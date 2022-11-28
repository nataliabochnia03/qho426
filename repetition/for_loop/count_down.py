print("How far are we from the cave?: ")
x = int(input())
for i in range(x,0,-1):
  x = x - 1 
  print(x, "steps remaining...")
  
print("We have reached the cave!")
