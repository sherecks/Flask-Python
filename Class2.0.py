from shelve import Shelf


class BookShelf:
    def __init__(self, *books):
        self.books = books

    def __str__(self):
        return f"O armário contém {len(self.books)} livros!"



class Book:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Book {self.name}"



book = Book("Senhor dos Anéis")
book_2 = Book("Star Wars")

shelf = BookShelf(book, book_2)
print(shelf)        
