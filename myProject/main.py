'''
Build a simple Library Management System using OOP in Python. Create a Book class (with title, author, ISBN) and a Library class to manage a collection of books. Implement methods to add_book, borrow_book, return_book, and display_available_books. Make sure a book can't be borrowed if it's already checked out. You can optionally add a search feature and a basic text menu for user interaction. Focus on clean class design and real OOP usage without overcomplicating it.
'''

from prettytable import PrettyTable


class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False


class Library:
    def __init__(self):
        self.books = []
        
    def add_book(self, title, author, isbn):
        book = Book(title, author, isbn)
        self.books.append(book)

    def borrow_book(self, isbn):
        for b in self.books:
            if isbn == b.isbn and b.is_borrowed == False:
                print(f"ISBN: {isbn}, book is borrowed!")
                b.is_borrowed = True
                break
        else:
            print("Book not found, come later.")
            return

    def return_book(self, isbn):
        for b in self.books:
            if isbn == b.isbn and b.is_borrowed == True:
                print(f"Book has been deposited, Thankyou!")
                b.is_borrowed = False
                break
        else:
            print("We never lend you this book.")
            return

    def display_available_books(self):
        if (len(self.books) != 0):
            title = [item.title for item in self.books]
            author = [item.author for item in self.books]
            isbn = [item.isbn for item in self.books]
            status = [
                "Borrowed" if item.is_borrowed else "Available" for item in self.books]

            table = PrettyTable()
            table.add_column("Title", title)
            table.add_column("Author", author)
            table.add_column("ISBN", isbn)
            table.add_column("Status", status)
            print(table)
        else:
            print("No book is available")

    def search_book(self, word):
        keyword = word.lower()
        matched = []
        for b in self.books:
            if (keyword in b.title.lower()) or (keyword in b.author.lower()) or (keyword in b.isbn.lower()):
                matched.append(b)
        else:
            if len(matched) == 0:
                print("No book found.")
                return

        title = [item.title for item in matched]
        author = [item.author for item in matched]
        isbn = [item.isbn for item in matched]
        status = [
            "Borrowed" if item.is_borrowed else "Available" for item in matched]

        table = PrettyTable()
        table.add_column("Title", title)
        table.add_column("Author", author)
        table.add_column("ISBN", isbn)
        table.add_column("Status", status)
        print(table)


lib = Library()

print("Welcome to E-Library!")
exit = False


while (not exit):
    user = int(input("Please enter a number to choose an action:\n\n1. Add a book\n2. Borrow a book\n3. Return a book\n4. Display available books\n5. Search books\n6. Exit\n\t:"))
    if(user in [1,2,3,4,5,6]):
        if(user==1):
            title=input("Enter title: ")
            author=input("Enter author: ")
            isbn=input("Enter ISBN: ")
            lib.add_book(title,author,isbn)
            print("Added!")
        elif(user==2):
            isbn=input("Enter ISBN: ")
            lib.borrow_book(isbn)
        elif(user==3):
            isbn=input("Enter ISBN: ")
            lib.return_book(isbn)
        elif(user==4):
            lib.display_available_books()
        elif(user==5):
            word=input("Enter Keyword: ")
            lib.search_book(word)
        else:
            print("Thankyou for visiting!")
            break
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    else:
        print("Invalid move")