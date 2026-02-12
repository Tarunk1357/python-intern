class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    # User
    def __str__(self):
        return f'"{self.title}" by {self.author} - ₹{self.price}'
  # developer
    def __repr__(self):
        return f'Book(title="{self.title}", author="{self.author}", price={self.price})'

# creating objects
book1 = Book("The Alchemist", "Paulo Coelho", 399)
book2 = Book("Atomic Habits", "James Clear", 499)

# printing calls __str__()
print(book1)
print(book2)
# printing inside a list - calls __repr__()
print([book1, book2])
