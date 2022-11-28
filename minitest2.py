def pokes():
  print("Here are the Pokemon!")
  me_poke = ["Pikachu", "Muk", "Arbok", "Charmander", "Mewtoo", "Ratatata", "Muk"]
  # for i in range(len(me_poke)):
  #   print(f"{me_poke[i]}", end = "***")

  # return me_poke
  print("***".join(me_poke))

def sounds(p = []):
  noises = {}
  for pokemon in set(p):
    
    print(f"What sound does {pokemon} make?")
    poke_sound = input()
    noises[pokemon] = poke_sound
  return noises

#print(sounds(["Koffing", "Mew"]))
# print(sounds(pokes()))

def store(sounds = {}):
  # f = open("pok_sounds.csv", "w")
  with open("pok_sounds.csv", "w") as f:
    for k, v in sounds.items():
      f.write(f"{k}, {v}\n")

# store(sounds(["Moyo","Ketchup"]))
pokes()


