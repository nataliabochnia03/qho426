def display(w):
  l = len(w)
  print("#"*(l+4))
  print("# " + w + " #")
  print("#"*(l+4))

def display_low(w):
  return w.lower()
def display_up(w):
  return w.upper()


def mirror(w):
  print(f"{w} | {w[::-1]}")

def repeat(w):
  print("How many times would you like to repeat the world?")
  n = int(input())
  for i in range(n):
    if i % 2 == 1:
        print(display_up(w))
    else:
      print(display_low(w))

def run():
    word = input("What is the world you would like to play with?")
    print("Choose one item from the menu:\n\n1-Display in a box\n2-Lower case\n3-Upper case\n4-Mirrored\n5-Repeat\n")
    response = int(input())
    if response == 1:
      display(word)
    elif response == 2:
      print(display_low(word))
    elif response == 3:
      print(display_up(word))
    elif response == 4:
      mirror(word)
    elif response == 5:
      repeat(word)
run()
  