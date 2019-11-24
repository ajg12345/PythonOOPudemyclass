#!/home/aaron4udemy/anaconda3/envs/udem/bin/python
class Library:

    def __init__(self,books):
        self.books  = books 
    
    def displayBooks(self):
        for book in self.books:
            print(book, end = ' ')
        print()
    
    def checkoutBook(self,book):
        if book in self.books:
            self.books.remove(book)
            print(book + ' has been checked out')
        else:
            print('book ' + book + ' not present in library')

    def returnBook(self, book):
        self.books.append(book)
        print('book ' + book + ' has been returned.')

class Customer:

    def requestBook(self):
        print("enter the book you want")
        self.book = input()
        return self.book

    def returnBook(self):
        print("enter the name of the book you are returning")
        self.book = input()
        return self.book

customer = Customer()
bookList = ['Dredd', 'Chess']
oplib = Library(bookList)
while True:
    print('Enter 1 to see available books')
    print('Enter 2 to see request a book')
    print('Enter 3 to see return a book')
    print('Enter 4 to see exit')
    choice = int(input())
    if choice == 1:
        oplib.displayBooks()
    elif choice == 3:
        returnedBook = customer.returnBook()
        oplib.returnBook(returnedBook)
    elif choice == 2:
        requestedBook = customer.requestBook()
        oplib.checkoutBook(requestedBook)
    elif choice == 4:
        quit()
