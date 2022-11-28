#A simple function definition to calculate area of a traingle
def calc_area(h = 2, b = 7):
  area = 0.5*h*b
  return area

#call to the function



#height = float(input("Enter the height of the triangle: "))
#base = float(input("Enter the base of the triangle: "))

#calc_area(5, 7)
#calc_area(height, base)
#calc_area(8, 9.3)
def run():
  print(calc_area())
  print(calc_area(8))
  print(calc_area(b=5))
  print(calc_area(6, 4))
#command + /     =skrot na komentarz
