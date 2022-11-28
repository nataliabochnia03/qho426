def likelihood():
  likelihoods = (50, 38, 27, 99, 4)
  return min(likelihoods), max(likelihoods)

#Q. Why does it need [0] and [1]? Shouldn't 0 be 50 and 1 38? as they are first and second values in the list? 


def run():
  prob = likelihood()
  print(f"Minimum likelihood of falling: {prob[0]}%")
  print(f"Maximum likelihood of falling: {prob[1]}%")

  
run()
