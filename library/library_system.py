from book import Book

class Library:
    def __init__(self)->None:
        self.books = []
    
    def add_book(self, title: str, author: str, isbn: str, status: str, year: int)-> None:
        new_book = Book(title, author, isbn, status, year)
        self.books.append(new_book)
    
    def list_books(self) -> list:
        for book in self.books:
            return f'{book}'


    def search_book(self, isbn_num: str)->str:
        for book in self.books:
            if isbn_num == book.isbn:
                return book 
        return 'Book not found in the library!'


lol = Library()

lol.add_book('lol', 'ok', '23','available', 20 )
lol.add_book('235', 'ok23', '2233','available', 230 )
lol.add_book('235', 'ok23', '23333s','available', 230 )
print(lol.search_book("23333s"))