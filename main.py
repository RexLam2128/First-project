'''
def calculate_paint(width, height):
  area = width * height
  paint = (area/11)* 1
  print("The paint required for  area ",area, " sqm is ", paint)



height = int(input("Please enter the height"))
width = int(input("Plese enter the width"))


calculate_paint(width, height)

'''

def students_books(students,books):
  output = students/books
  print("The output is ",output)

students = int(input("Please enter the number of students"))

books = int(input("Please enter the number of books"))

students_books(students,books)