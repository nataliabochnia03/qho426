import matplotlib.pyplot as plt
import matplotlib.animation as animation
#bob=fig
bob, ax = plt.subplots()

def animate(frame):
  ax.cla()
  ax.set_xlim(0,10)
  ax.set_ylim(0,100)
  ax.plot(frame, frame**2,"bo")

def run():
  x = animation.FuncAnimation(bob, animate, frames = 10, interval = 100, repeat = False)
  plt.show()

  
run()
