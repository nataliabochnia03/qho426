def sum_weights(Beep_weight, Boop_weight):
  total_sum = Beep_weight + Boop_weight
  return total_sum

def calc_avg_weight(Beep_weight, Boop_weight):
  avg_weight = (Beep_weight + Boop_weight) / 2
  return avg_weight

def run():
  print("What is the weight of Beep?")
  Beep_weight = float(input())

  print("What is the weight of Bop?")
  Boop_weight = float(input())

  print("What would you like to calculate (sum or average)?: ")
  action = input()

  if (action == "sum"):
    answer = sum_weights(Beep_weight, Boop_weight)
    print("The sum of Beep and Bop's weight is: ",answer)

  elif (action == "average"):
    answer = calc_avg_weight(Beep_weight, Boop_weight)
    print("The average of Beep and Bop's weight is: ", answer)
  else:
    print("I am not sure what you would like to do.")
run()
