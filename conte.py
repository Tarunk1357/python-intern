class DatabaseConnection:
    def __enter__(self):
        print("Database Connected")

    def __exit__(self, exc_type, exc_value, traceback):
        print("Database Closed")

# use with 
with DatabaseConnection():
    print("performing query")
