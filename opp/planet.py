from human import Human
from robot import Robot

class Planet:

  def __init__(self):
    self.inhabitants = []

  def __str__(self):
    return f"On this plante we have following inhabitants: {self.inhabitants}"
  
  def __repr__(self):
    return f"inhabitants: {self.inhabitants}"

  def add_inhabitant(self, inhabitant):
    self.inhabitants.append(inhabitant)

  def remove_inhabitant(self, inhabitant):
    if inhabitant in self.inhabitants:
      self.inhabitants.remove(inhabitant)


  # def add_robot(self, robo):
  #   self.inhabitants['robots'].append(robo)

  # def remove_robot(self, robo):
  #   if robo in self.inhabitants['robots']:
  #     self.inhabitants['robots'].remove(robo)

if __name__ == "__main__":
    Beep = Robot("Beep")
    Alessandro = Human("Alessandro", 22)
    p1 = Human("Anca")
    p2 = Human("Larry")
    r1 = Robot("RoboCop")
    r2 = Robot("Terminator", 40)
    Earth = Planet()
    print(Earth)
    Earth.add_inhabitant(Alessandro)
    Earth.add_inhabitant(p1)
    Earth.add_inhabitant(p2)
    Earth.add_inhabitant(r1)
    Earth.add_inhabitant(Beep)
    print(Earth)
    Earth.remove_inhabitant(p2)
    Earth.remove_inhabitant(r1)
    Earth.add_inhabitant(r2)
    print(Earth)
    
  



    

