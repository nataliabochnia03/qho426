import matplotlib.pyplot as plt
import matplotlib.animation as animation
#bob=fig
bob, ax = plt.subplots()

def animate(frame):
  ax.set_xlim(0,10)
  ax.set_ylim(0,10)
  ax.plot(frame, frame, "ro")


def run():
  x = animation.FuncAnimation(bob, animate, frame = 10, interval = 1000)
  plt.show()

  
run()
