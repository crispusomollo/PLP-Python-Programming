# Base Class: Book
class Book:
    def move(self):
        print("The book is placed on the shelf.")

# Subclass: EBook
class EBook(Book):
    def move(self):
        print("The e-book is stored in the cloud.")

# Subclass: Audiobook
class Audiobook(Book):
    def move(self):
        print("The audiobook is playing in your app.")

# Polymorphism in Action
books = [Book(), EBook(), Audiobook()]

for book in books:
    book.move()
