# Base Class: Book
class Book:
    def __init__(self, title, author, pages, genre):
        self.title = title
        self.author = author
        self.pages = pages
        self.genre = genre

    def get_description(self):
        return f"'{self.title}' by {self.author}, {self.pages} pages, Genre: {self.genre}"

    def read(self):
        print(f"You are reading '{self.title}'.")

# Subclass: EBook
class EBook(Book):
    def __init__(self, title, author, pages, genre, file_size, format_type):
        super().__init__(title, author, pages, genre)
        self.file_size = file_size
        self.format_type = format_type

    def get_description(self):
        base_description = super().get_description()
        return f"{base_description} (E-Book: {self.file_size}MB, {self.format_type} format)"

    def download(self):
        print(f"Downloading '{self.title}' as a {self.format_type} file...")

# Subclass: Audiobook
class Audiobook(Book):
    def __init__(self, title, author, pages, genre, duration, narrator):
        super().__init__(title, author, pages, genre)
        self.duration = duration
        self.narrator = narrator

    def get_description(self):
        base_description = super().get_description()
        return f"{base_description} (Audiobook: {self.duration} hours, Narrated by {self.narrator})"

    def play(self):
        print(f"Playing the audiobook '{self.title}', narrated by {self.narrator}.")

# Create instances
paperback = Book("To Kill a Mockingbird", "Harper Lee", 324, "Classic Fiction")
ebook = EBook("1984", "George Orwell", 328, "Dystopian Fiction", 1.2, "EPUB")
audiobook = Audiobook("Becoming", "Michelle Obama", 400, "Memoir", 19.5, "Michelle Obama")

# Use methods
print(paperback.get_description())
paperback.read()

print(ebook.get_description())
ebook.download()

print(audiobook.get_description())
audiobook.play()
