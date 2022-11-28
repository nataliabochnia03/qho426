print("How many bars should be charged?")
cables_to_charge = int(input())
cables_charged = 0
print()

while (cables_to_charge>cables_charged):
  cables_charged += 1
  print("Charging: ", "█" * cables_charged)
    
print("The battery is fully charged.")    
  