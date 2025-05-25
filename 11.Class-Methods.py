class Book:
   
    total_books = 0

    def __init__(self, title, author):
        self.title = title
        self.author = author
     
        Book.increment_book_count()
        print(f"[Book] Added: '{self.title}' by {self.author}")

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1
        print(f"[Book] Total books now: {cls.total_books}")

    @classmethod
    def get_total_books(cls):
        return cls.total_books



def main():
    print("Adding books to the library:")
    book1 = Book("1984", "George Orwell")
    book2 = Book("To Kill a Mockingbird", "Harper Lee")
    book3 = Book("The Great Gatsby", "F. Scott Fitzgerald")

    print(f"\nTotal books in library: {Book.get_total_books()}")


if __name__ == "__main__":
    main()
