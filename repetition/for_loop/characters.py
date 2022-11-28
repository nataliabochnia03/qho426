# print("Please enter a word")
# user_word = input()

# for position in range(0, len(user_word), 1):
#     print(user_word[position])

print("What strange markings do you see?: ")
response = input()
print("Identifying...")
#len w tym wypadku podaje nam koncowa dlugosc bazujac na ilosci liter w naszym slowie. Czyli jesli bedziemy miec kot to bedziemy miec tylko 3 linijki tekstu, jesli wpiszemy papuga98 to bedziemy miec juz 8 linijek.
for i in range(0,len(response), 1):
  # w tym przypadku to 'i' w [] pozwala nam rozdzielic kazdy character w stringu. Zaluzmy ze nasz input to ^&£ gdyby go nie bylo to kod wygladal by nastepujaco 
  #Index 0 : ^&£
  #Index 1 : ^&£
  #Index 2 : ^&£
  #Jednak dzieki temu, ze go mamy to kod wyglada tak 
  #Index 0 : ^
  #Index 1 : &
  #Index 2 : £

  print("Index", i, ":", response[i])
