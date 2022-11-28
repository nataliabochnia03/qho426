import matplotlib.pyplot as plt 

def both_Ts():
  x = [2,2, 1, 1, 4, 4, 3, 3]
  y = [2, 6, 6, 7, 7, 6, 6, 2]
  x2 = [1,1,5,5,10,10,14,14,1]
  y2 = [1,5,5,12,12,5,5,1,1]

  plt.plot(x, y, "-r^")
  plt.plot(x2, y2, "Db--")
  plt.show()

def separate_Ts():
  fig, (ax1, ax2) = plt.subplots(2)
  x = [2,2, 1, 1, 4, 4, 3, 3]
  y = [2, 6, 6, 7, 7, 6, 6, 2]
  x2 = [1,1,5,5,10,10,14,14,1]
  y2 = [1,5,5,12,12,5,5,1,1]
  ax1.plot(x,y,"ys-.")
  ax2.plot(x2,y2, "g-")
  # sprawianie ze sa takiej samej wielkosci : 
  ax1.set_xlim(0,15)
  ax2.set_xlim(0,15)
  plt.show()

separate_Ts()