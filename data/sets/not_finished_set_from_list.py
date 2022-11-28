def observed():
  observations = []
  for i in range(7):
    obs = input("Please enter an observation: ")
    print(obs)
  observations.add((obs))
  return observations

def run():
  print("Counting observations...)
  ogog = observed()
  
