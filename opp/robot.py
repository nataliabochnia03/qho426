from inhabitant import Inhabitant
class Robot(Inhabitant):

  MAX_ENERGY = 100


  def __init__(self, name = "Beep", age = 0):
      super().__init__(name, age)
      self.laws = "Serve and Obey!"
    # self.name = name
    # self.age = age
    # self.energy = 0

  def __repr__(self):
    return f'robot(name={self.name}, age={self.age})'

  def __str__(self):
    return f'Robot {self.name} is {self.age} years old.'

  def the_laws(self):
    return self.laws

  # def grow(self, name ="Beep", age = 0):
  #   self.age += 1

  # def eat(self, amount):
  #   self.energy += amount
  #   if self.energy > Robot.MAX_ENERGY:
  #     self.energy = Robot.MAX_ENERGY

  # def move(self, distance):
  #   self.energy -= distance
  #   if self.energy < 0:
  #     self.energy = 0



if (__name__ == "__main__"):
  human = Robot("Wall-E")
  human.display()
  print(human)
  print(repr(human))
  human.move(83)
  print(human)
  human.eat(59)
  print(human)
  