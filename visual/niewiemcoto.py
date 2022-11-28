import matplotlib.pyplot as plt

def coordinate():
  x = int(input("Enter the x value: "))
  y = int(input("Enter the y value: "))
  return (x, y)

def path():
  print("Retrieving path...")
  x_values = []
  y_values = []
  for i in range(4):
    data = coordinate()
    x_values.append(x)
    y_values.append(y)
    
