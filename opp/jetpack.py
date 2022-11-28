from tech import Tech

class Jetpack(Tech):


  def __str__(self):
    return "It's a Jetpack"

  def __repr__(self):
    return "jetpack()"


  def activate(self):
    print("Brummmm! (Jetpack Activated)")

  def deactivate(self):
    print("Oufff! (Jetpack off)")

  def fly(self, distance = 1):
    print(f"We went up by {distance}m up!")

if __name__ == "__main__":
  j = Jetpack()
  j.activate()
  j.fly()
  j.fly(5)
  j.fly(1000000)
  j.deactivate()
