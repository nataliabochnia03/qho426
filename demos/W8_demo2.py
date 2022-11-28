import matplotlib.pyplot as plt

def coffee_sleep():
  coffee = []
  sleep = []
  for i in range(7):
    coffee.append(int(input("Enter the amout of coffee per week: ")))
    sleep.append(int(input("Enter your average sleep length: ")))
  return coffee, sleep 


def movie():
  movies = {}
  for i in range(7):
    movie = input("Enter your favourite movie genre: ")
    movies[movie] = movies.get(movie, 0) + 1
  return movies

def music():
  songs = {}
  for i in range(7):
    song = input("Enter your favourite song genre: ")
    songs[song] = songs.get(song, 0) + 1
  return songs


def  MM_vs_DD():
  mm = 0
  dd = 0
  for i in range(7):
    ans  = input("Who wins? Micky Mouse or Donald Duck ")
    if ans.upper() == "DD":
      dd += 1
    elif ans.upper() == "MM":
      mm += 1

  return [mm, dd]

def run():
  fig = plt.figure()

  ax1 = fig.add_subplot(2,2,1)
  ax2 = fig.add_subplot(2,2,2)
  ax3 = fig.add_subplot(2,2,3)
  ax4 = fig.add_subplot(2,2,4)

  c_s = coffee_sleep()
  ms = movie()
  lista = []
  for k in ms:
    dist = float(input("How much explosion? "))
    lista.append(dist)
  ss = music()
  ax1.plot(c_s[0], c_s[1], "rx")
  ax2.pie(ms.values(),labels = ms.keys(), autopct = "%.f%%", explode = [])
  ax3.pie(ss.values(), labels = ss.keys(), autopct = "%1.1f%%")
  ax4.bar(["Donald Duck", "Mickey Mouse"], MM_vs_DD())

  plt.show()

run()