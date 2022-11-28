import csv

def writing_csv():
  with open("d.csv", "w") as data:
      csv_writer = csv.writer(data, delimiter = "@")
      for i in range(3):
          print("Enter the name")
          n = input()
          print("Enter the age")
          a = input()
          print("Enter the favourite album")
          album = input()
          csv_writer.writerow(list((n, a, album)))
def reading_csv():
  with open("d.csv") as bob:
    csv_reader = csv.reader(bob)
    for line in csv_reader:
        print()
        for item in line:
          print(item, end = ",")
          
writing_csv()
reading_csv()







#___________________________
# f = open("computing.txt")

# # x = input("Sing me a song!")

# # f.write(x)
# # f.write("\n")

# # lista =["Alessandro\n", "Dawid\n", "Wesley\n", "Fikret\n", "Orsi\n"]
# # f.write("\n")
# # f.writelines(lista)

# #python blended colours
# # print(f"\033[94m{f.readlines()}\033[0m")

# f.close()