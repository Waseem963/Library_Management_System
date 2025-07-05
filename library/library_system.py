from book import Book

class Library:
    def __init__(self)->None:
        self.__books = []
    
    def __str__(self) -> str:
        return f"Library contains {len(self.books)} books."
    
    def __repr__(self) -> str:
        return f"Library({len(self.books)})."
    
    @property
    def books(self) -> list:
            return self.__books

    def add_book(self, title: str, author: str, isbn: str, status: str, year: int)-> None:
        if any(book.isbn == isbn for book in self.books):
            raise ValueError(f"Book with ISBN {isbn} already exists.")
        
        new_book = Book(title, author, isbn, status, year)
        self.books.append(new_book)
    
    def list_books(self) -> None:
        if not self.books:
            return "Library is empty."
        
        result = ""
        for book in self.books:
            result += f"{book}\n"
        return result


    def search_book(self, isbn_num: str)->Book:
        for book in self.books:
            if isbn_num == book.isbn:
                return book 
        raise LookupError(f"Book with ISBN {isbn_num} not found.")


    def remove_book(self, isbn_num: str)-> str:
        for book in self.books:
            if isbn_num == book.isbn:
                self.books.remove(book)
                return f'Book {book.title} with ISBN {book.isbn} has been removed'
            
        raise LookupError(f"Book with ISBN {isbn_num} not found.")
             

