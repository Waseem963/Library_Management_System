from book import Book

class Library:
    """
    This class has library system such as adding books and list books.

    Attributes:
    Books (List): Save books objects to the library.

    Methods:
    add_book(): Add a book to the library.
    list_books(): List all books in the library.
    search_book(): Search on a spesific isbn book in the library.
    remove_book(): Remove a book from the library.

    """
    def __init__(self)->None:
        self.__books = []
    
    def __str__(self) -> str:
        return f"Library contains {len(self.books)} books."
    
    def __repr__(self) -> str:
        return f"Library({len(self.books)})."
    
    @property
    def books(self) -> list:
            return self.__books

    # Add books to the library
    def add_book(self, title: str, author: str, isbn: str, status: str, year: int)-> None:
        if any(book.isbn == isbn for book in self.books):
            raise ValueError(f"Book with ISBN {isbn} already exists.")
        
        new_book = Book(title, author, isbn, status, year)
        self.books.append(new_book)
    
    # Print books from the library.
    def list_books(self) -> None:
        if not self.books:
            return "Library is empty."
        
        result = ""
        for book in self.books:
            result += f"{book}\n"
        return result

    # Search about a book using its ISBN number
    def search_book(self, isbn_num: str)->Book:
        for book in self.books:
            if isbn_num == book.isbn:
                return book 
        raise LookupError(f"Book with ISBN {isbn_num} not found.")

    # Remove books from the library.
    def remove_book(self, isbn_num: str)-> str:
        for book in self.books:
            if isbn_num == book.isbn:
                self.books.remove(book)
                return f'Book {book.title} with ISBN {book.isbn} has been removed'
            
        raise LookupError(f"Book with ISBN {isbn_num} not found.")
             

