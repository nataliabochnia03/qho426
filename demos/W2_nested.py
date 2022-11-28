salary = float(input("Enter your salary: "))
years = int(input("How long are you with the company? "))

if years > 2: 
  if salary < 25000:
     salary *=1.1
  else:
    salary+=100
    print(f"Your new salary is now £{salary}")
elif years > 1:
  print("No salary increase for you!")
else: 
  if salary < 15000:
    print("Apologies, this was an error. You shall earn £20000 ")
    salary = 20000
print("Let us all work for the good of the corporation")
