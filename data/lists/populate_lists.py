def directions():
  directions = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
  return directions

def menu():
  print("Please select the direction:")
  direct = directions()
  for index in range(len(direct)):
     print("{}: {}".format(index, direct[index]))
  index = int(input())
  return direct[index]

def run():
  route = []
  print("Working out escape route...")
  for i in range(5):
    route.append(menu())
  print(f"Escape route: {route}")

run()

