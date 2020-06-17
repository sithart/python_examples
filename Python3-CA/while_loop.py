all_students = ["Alex", "Briana", "Cheri", "Daniele", "Dora", "Minerva", "Alexa", "Obie", "Arius", "Loki"]
students_in_poetry = []


while len(students_in_poetry) < 6:
  name = all_students.pop()
  students_in_poetry.append(name)

print(students_in_poetry)
