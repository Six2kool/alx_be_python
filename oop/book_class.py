# book_class.py

class Book:
    # This is the constructor → runs when you create a new book
    def __init__(self, title, author, year):
        self.title = title          # save the title inside the book
        self.author = author        # save the author
        self.year = year            # save the year
        print(f"New book created: {title}")  # optional, just to see it born

    # Friendly way to print the book
    def __str__(self):
        return f"{self.title} by {self.author}, published in {self.year}"

    # Programmer/official way → shows how to recreate the exact same book
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.year})"

    # This runs when the book gets deleted with "del"
    def __del__(self):
        print(f"Deleting {self.title}")