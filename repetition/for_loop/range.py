print("What level of brightness is required? please enter an even number: ")
light = int(input())
print("Adjusting brightness...")
#'i' to ostateczna wartosc 'range'
for i in range(2,light+1,2):
  print("Beep's brightness level:", "*" * i)
  print("Bop's brightness level:", "*" * i)
