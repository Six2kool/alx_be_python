# Parent class - every book has this stuff
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    # This controls how the book looks when printed
    def __str__(self):
        return f"Book: {self.title} by {self.author}"


# Child class 1 - Digital book (inherits from Book)
class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)   # Get title & author from parent
        self.file_size = file_size        # Extra thing only EBook has

    def __str__(self):
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


# Child class 2 - Paper book (also inherits from Book)
class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)   # Reuse parent's code
        self.page_count = page_count

    def __str__(self):
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


# The backpack that holds all books
class Library:
    def __init__(self):
        self.books = []   # Empty list at first

    def add_book(self, book):
        self.books.append(book)   # Put book inside the backpack

    def list_books(self):
        for book in self.books:
            print(book)   # Python automatically uses the right __str__!