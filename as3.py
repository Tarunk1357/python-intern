class book:
    def __init__(self,title,author):
        self.title=title
        self.author=author
    def display_book(self):
        print("The book title is",self.title)
        print("and the author is",self.author)

class issuebook(book):
    def __init__(self,title,author,issued_to,issued_date):
        super().__init__(title,author)
        self.issued_to=issued_to
        self.issued_date=issued_date
    def display_issued_book(self):
        self.display_book()
        print("The book is issued to",self.issued_to)
        print("on date",self.issued_date)

issuebook=issuebook("The Alchemist","Paulo Coelho","Alice","2024-06-01")

issuebook.display_issued_book()