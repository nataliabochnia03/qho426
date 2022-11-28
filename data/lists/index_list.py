def movements():
  path = ["Move Forward", 10, "Move Backward", 5, "Move Left", 3, "Move Right", 1]
  return path

def run():
  print("Moving...")
  path = movements()
  for i in range(0, len(path), 2):
    print(f"{path[i]} for {path[i+1]} steps")

#range(start, end, steps)
#range(end)
#range(start, end)

    #below is another way of doing this
  # print(f"{path[0]} for {path[1]} steps")
  # print(f"{path[2]} for {path[3]} steps")
  # print(f"{path[4]} for {path[5]} steps")
  # print(f"{path[6]} for {path[7]} steps")

run()
