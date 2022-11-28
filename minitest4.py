from abc import ABC, abstractmethod

class Pet(ABC):

  def __init__(self, name = "Zonk"):
    self.name = name
    self.age= 1
    self.smell = True

#creating a abstract class, we always need to put pass at the end and import abstractmethod

  @abstractmethod
  def sound():
    pass

class Dog(Pet):
  def __init__(self, name, toy):
    self.toy = toy
    self.daily_walks = 3
    super().__init__(name)

#repr is formal representation
  def __repr__(self):
    return f"dog(name = {self.name}, toy = {self.toy}, age = {self.age}, daily_walks = {self.daily_walks})"

  def __str__(self):
    return f"My doggo is called {self.name}, it is {self.age} years old, and I walk it {self.daily_walks} times"
#don't forget to put self in the brackets even if it is not said to do so!!!
  def get_age(self):
    return
#if you have a return value simply write "return" but if you have return nothing, just write print()
  def sound(self):
    print("Woooof-Wooof")

  def wash(self):
    self.smell = False #Assuming washing removes the smell 


class Husband(Pet):

  def __init__(self, name, job):
    self.job = job
    super().__init__(name)


  def __repr__(self):
    return f"husband(name = {self.name}, job = {self.job}, age = {self.age}, smell = {self.smell})"

  def __str__(self):
    return f"The husband called {self.name}, is {self.age} old, and he works as {self.job}"

  def sound(self):
    print("Ufffff")
    print("Bring me a can")
    print("Yes my love:)))")

class Jobless_Husband(Husband):

  def __init__(self,name,job = None):
    super.__init__(name, job)

  def __repr__(self):
    return f"jobless_husband(name = {self.name}, job = {self.job}, age = {self.age}, smell = {self.smell})"

  def __str__(self):
    return f"The jobless husband called {self.name}, is {self.age} old, and he doesn't work!"

  def get_job(self, j_name):
    self.job = j_name

#Testing

if __name__ == "__main__":
  psotka = Dog("Psotka", "Woody")
  jimmy = Husband("Jimmy", "Accountant")
  ted = Jobless_Husband("Ted")
  psotka.sound()
  print(psotka)
  psotka.age+=1
  print(psotka)
  jimmy.sound()
  print(jimmy)
  ted.sound()
  print(ted)
  ted.get_job("KFC clerk")
