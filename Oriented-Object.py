class Student:
  def __init__(self):
    self.name = "Pietra"
    self.notas = (5, 10, 4, 7, 6, 5)

  def average(self):
    return sum(self.notas) / len(self.notas)


student = Student()
print(f"Nome: {student.name}")
print(f"Notas: {student.notas}")
print(f"Media: {student.average()}")
