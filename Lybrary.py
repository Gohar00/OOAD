from abc import ABC, abstractmethod


class Library(ABC):
    @abstractmethod
    def search_book(self, title):
        pass

    @abstractmethod
    def borrow_book(self, book, borrower):
        pass

    @abstractmethod
    def return_book(self, book, borrower):
        pass


class Book:
    def __init__(self, title, author, publication_date):
        self.title = title
        self.author = author
        self.publication_date = publication_date

    @abstractmethod
    def get_type(self):
        pass


class FictionBook(Book):
    def __init__(self, title, author, publication_date):
        super().__init__(title, author, publication_date)

    def get_type(self):
        return "Fiction"


class NonFictionBook(Book):
    def __init__(self, title, author, publication_date):
        super().__init__(title, author, publication_date)

    def get_type(self):
        return "Non-fiction"


class Borrower:
    def __init__(self, name, contact_info):
        self.name = name
        self.contact_info = contact_info
        self.borrowing_history = []
        self.borrowed_books = []

    def borrow_book(self, library, title):
        book = library.search_book(title)
        if book is not None:
            library.borrow_book(book, self)
            self.borrowed_books.append(book)
            print(f"{self.name} has borrowed {book.title} by {book.author}.")
        else:
            print(f"{title} is not available in the library.")

    def return_book(self, library, book):
        if book in self.borrowed_books:
            library.return_book(book, self)
            self.borrowed_books.remove(book)
            self.borrowing_history.append(book)
            print(f"{self.name} has returned {book.title}.")
        else:
            print(f"{self.name} did not borrow {book.title}.")

    def view_borrowing_history(self):
        borrowing_history = []
        for book in self.borrowing_history:
            borrowing_history.append((book.title, book.author))
        return borrowing_history


class Librarian:
    def __init__(self, name, contact_info):
        self.name = name
        self.contact_info = contact_info

    def add_book(self, library, book):
        library.add_book(book)
        print(f"{book.title} by {book.author} has been added to the library.")

    def remove_book(self, library, book):
        library.remove_book(book)
        print(f"{book.title} by {book.author} has been removed from the library.")


class PublicLibrary(Library):
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        self.books.remove(book)

    def search_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None

    def borrow_book(self, book, borrower):
        self.books.remove(book)

    def return_book(self, book, borrower):
        self.books.append(book)


from library import *

# Create some books
book1 = FictionBook("The Great Gatsby", "F. Scott Fitzgerald", "1925")
book2 = NonFictionBook("The Selfish Gene", "Richard Dawkins", "1976")
book3 = FictionBook("To Kill a Mockingbird", "Harper Lee", "1960")

# Create some borrowers
borrower1 = Borrower("John Smith", "jsmith@gmail.com", "555-1234")
borrower2 = Borrower("Jane Doe", "jdoe@gmail.com", "555-5678")

# Create a librarian
librarian1 = Librarian("Mary Johnson", "mjohnson@gmail.com", "555-4321")

# Add books to the library
librarian1.add_book(book1)
librarian1.add_book(book2)
librarian1.add_book(book3)

# Borrow a book
librarian1.borrow_book(book1, borrower1, 14)

# Search for available books
available_books = borrower1.search_books(librarian1.get_books(), "Fiction")
print("Available books:")
for book in available_books:
    print(book.get_title())

# Return a book
librarian1.return_book(book1, borrower1)

# View borrowing history
borrowing_history = borrower1.get_borrowing_history()
print("Borrowing history:")
for book, duration in borrowing_history:
    print(book.get_title(), duration)
