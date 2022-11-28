#nie zastosowalam loop ale i tak dziala jak powinno 

def cross_bridge(steps):
  print("Crossed step\n "* steps,)
  if steps > 5:
    print("The bridge is collapsing!")
  else:
    print("We must keep going!")
cross_bridge(3)
cross_bridge(6)

