class Book:
    def __init__(self,title,author):
        self.is_borrowed=False
        self.title=title
        self.author=author

    def borrow(self):
        self.is_borrowed=True
        print(f"The book titled {self.title} written by {self.author} is borrowed from the library.")


    def return_book(self):
        self.is_borrowed=False
        print(f"The book titled {self.title} written by {self.author} is returned back to the library.")


book1=Book("Harry Potter","J.K.Rowling")
book2=Book("Percy Jackson","Rick Riordan")
book3=Book("Persian Fire","Tom Holland")
book1.borrow()
book2.borrow()
book3.borrow()
book1.return_book()
book2.return_book()
book3.return_book()