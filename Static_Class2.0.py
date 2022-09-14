from typing import Type


class Book:
  Types = ("Hardcover", "Paperback")

  def __init__(self, name, book_type, weight):
    self.name = name
    self.book_type = book_type
    self.weight = weight

  def __repr__(self):
    return f"Livro {self.name}, {self.book_type}, Peso: {self.weight}"

  @classmethod
  def hardcover(cls, name, page_weight):
    return Book(name, Book.Types[0], page_weight + 100)

  @classmethod
  def paperback(cls, name, page_weight):
    return Book(name, Book.Types[1], page_weight)  

book = Book.hardcover("Senhor dos Aneis", 1500)
light = Book.paperback("Star Wars", 950)

print(book)
print(light)

