class Student:
  def __init__(self, name, notas):
    self.name = name
    self.notas = notas

  def average(self):
    return sum(self.notas) / len(self.notas)


student = Student("Pietra", (10, 8, 7, 5, 9, 7))

student2 = Student("João Pedro", (7, 6, 5, 6, 8, 7))

print(f"Nome: {student.name}")
print(f"Notas: {student.notas}")
print(f"Media: {student.average()}")

print(f"Nome: {student2.name}")
print(f"Notas: {student2.notas}")
print(f"Media: {student2.average()}")
