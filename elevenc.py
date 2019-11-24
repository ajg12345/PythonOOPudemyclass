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

bookList = ['Dredd', 'Chess']
oplib = Library(bookList)
oplib.displayBooks()
oplib.checkoutBook('Moby Dick')
oplib.displayBooks()
oplib.checkoutBook('Chess')
oplib.displayBooks()
oplib.returnBook('Chess')
oplib.displayBooks()
