print("How many rows should I have?: ")
rows = int(input())

print("How many columns should I have?: ")
columns = int(input())

for r in range(0, rows, 1):
  for c in range(0, columns, 1):
    print(":-)", end="")
  print()
