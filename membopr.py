class Library:
    
    def __init__(self, books):
        self.books = books
    def __contains__(self, item):
        return item in self.books

library = Library(["Python Basics", "Data Science", "AI Fundamentals"])

#in operator
print("Python Basics" in library)   # True
print("Machine Learning" in library)  # False