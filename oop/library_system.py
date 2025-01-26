class Book:
    def __init__(self, title, author):
        """Constructor: Initializes a Book instance."""
        self.title = title
        self.author = author

    def __del__(self):
        """Destructor: Prints a message upon object deletion."""
        print(f"Deleting '{self.title}'")

    def __str__(self):
        """String representation: For user-friendly output."""
        return f"Book: {self.title} by {self.author}"

    def __repr__(self):
        """Official representation: Used for debugging and recreating the object."""
        return f"Book('{self.title}', '{self.author}')"

class EBook(Book):
    def __init__(self, title, author, file_size):
        """Constructor: Initializes an EBook instance."""
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"

    def __repr__(self):
        return f"EBook('{self.title}', '{self.author}', {self.file_size})"

class PrintBook(Book):
    def __init__(self, title, author, page_count):
        """Constructor: Initializes a PrintBook instance."""
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"

    def __repr__(self):
        return f"PrintBook('{self.title}', '{self.author}', {self.page_count})"

class Library:
    def __init__(self):
        """Constructor: Initializes the Library with an empty list of books."""
        self.books = []

    def add_book(self, book):
        """Adds a Book, EBook, or PrintBook instance to the library."""
        if isinstance(book, Book):
            self.books.append(book)
        else:
            raise TypeError("Only instances of Book, EBook, or PrintBook can be added.")

    def list_books(self):
        """Prints details of each book in the library."""
        for book in self.books:
            print(book)
