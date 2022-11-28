def directions():
  directions = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
  return directions


def menu():
  print("Please select a direction:")
  direct = directions()
  for index in range(len(direct)):
    print(f"{index}:{direct[index]}")

def run ():
  menu()

run()