class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_available = True


class Patron:
    def __init__(self, patron_id, name):
        self.patron_id = patron_id
        self.name = name
        self.borrowed_books = []


class Library:
    def __init__(self):
        self.books = {}
        self.patrons = {}

    def add_book(self, book):
        self.books[book.book_id] = book
        print("Book added successfully.")

    def register_patron(self, patron):
        self.patrons[patron.patron_id] = patron
        print("Patron registered successfully.")

    def borrow_book(self, book_id, patron_id):
        if book_id not in self.books:
            print("Book not found.")
            return

        if patron_id not in self.patrons:
            print("Patron not found.")
            return

        book = self.books[book_id]
        patron = self.patrons[patron_id]

        if not book.is_available:
            print("Book is already borrowed.")
            return

        book.is_available = False
        patron.borrowed_books.append(book)
        print(f"{patron.name} borrowed '{book.title}'.")

    def return_book(self, book_id, patron_id):
        if patron_id not in self.patrons:
            print("Patron not found.")
            return

        patron = self.patrons[patron_id]

        for book in patron.borrowed_books:
            if book.book_id == book_id:
                book.is_available = True
                patron.borrowed_books.remove(book)
                print(f"'{book.title}' returned successfully.")
                return

        print("This patron has not borrowed this book.")

    def display_books(self):
        print("\nBooks in Library:")
        for book in self.books.values():
            status = "Available" if book.is_available else "Borrowed"
            print(f"{book.book_id} - {book.title} by {book.author} ({status})")

library = Library()

while True:
    print("\n===== Library Management System =====")
    print("1. Add Book")
    print("2. Register Patron")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Display Books")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        book_id = input("Enter Book ID: ")
        title = input("Enter Book Title: ")
        author = input("Enter Author: ")

        book = Book(book_id, title, author)
        library.add_book(book)

    elif choice == "2":
        patron_id = input("Enter Patron ID: ")
        name = input("Enter Patron Name: ")

        patron = Patron(patron_id, name)
        library.register_patron(patron)

    elif choice == "3":
        book_id = input("Enter Book ID: ")
        patron_id = input("Enter Patron ID: ")

        library.borrow_book(book_id, patron_id)

    elif choice == "4":
        book_id = input("Enter Book ID: ")
        patron_id = input("Enter Patron ID: ")

        library.return_book(book_id, patron_id)

    elif choice == "5":
        library.display_books()

    elif choice == "6":
        print("Thank you for using the Library Management System.")
        break

    else:
        print("Invalid choice. Please try again.")
