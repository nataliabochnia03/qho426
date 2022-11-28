

#Test1
#Delete all  the fucntion calls after!!
def fav_movie():
  print("What is your favourite movie?")
  m = input()
  print(f"{m} is terrible! How could you like it so much?")


def imdb_rating(rating):
  if rating > 7:
    print("Let's watch it!")
  else:
    print("not gonna waste my time on that")
  print("I hope you agree")

def binge(numb):
  for i in range(numb):
    print(f"Oh-yeah! #{i+1}")
  print(f"There are {numb} episodes in the series")
