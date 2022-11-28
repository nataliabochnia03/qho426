from inhabitant import Inhabitant
class Human(Inhabitant):

  MAX_ENERGY = 100

  def __init__(self, name ="Human", age = 0):
    super().__init__(name, age)
    self.clothing = []
    
    # self.name = name
    # self.age = age
    # self.energy = Human.MAX_ENERGY

  def __repr__(self):
      return f'Human(name={self.name}, age={self.age}), energy: {self.energy}'

  def __str__(self):
    return f'Robot {self.name} is {self.age} years old and has {self.energy} energy left.'
  
  def dress(self, clothing):
    self.clothing.append(clothing)

  def undress(self, clothing):
    self.clothing.remove(clothing)
    

  # def grow(self):
  #     self.age += 1

  # def eat(self, amount):
  #   self.energy += amount
  #   if self.energy >      Human.MAX_ENERGY:
  #     self.energy = Human.MAX_ENERGY

  # def move(self, distance):
  #   self.energy -= distance
  #   if self.energy < 0:
  #     self.energy = 0

if (__name__ == "__main__"):
  human = Human()
  human.display()
  print(human)
  print(repr(human))
  print(human)
  human.move(27)
  print(human)
  human.eat(11)
  human.eat(2)
  print(human)

  