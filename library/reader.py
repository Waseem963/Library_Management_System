from user import User

class Reader(User):
    """
    This class represents Reader users that are registerd in the library.

    Attributes:
    super().__init__(name, user_id) (str, str): inheretence attributes from User class (name, user_id).
    borrowed_books (int): Count borrowed books from the library.

    Method:
    show_role(): Return user role (Reader).
    borrow_book(): Add 1 to borrowed books to count how many books has been borrowed from the library.
    return_book(): Subtract 1 from borrowed books when a user return a book.

    
    
    
    """
    def __init__(self, name: str, user_id: str, borrowed_books : int) -> None:
        super().__init__(name, user_id)
        self.__borrowed_books  = borrowed_books 

    def __str__(self)-> str:
        return f"Name: {self.name}, User ID: {self.user_id}, borrowed_books: {self.borrowed_books}"
    
    def __repr__(self)-> str:
        return f"<Reader(name={self.name!r}, user_id={self.user_id!r}, borrowed_books={self.borrowed_books!r})>"

        
    # Identify reader as reader role
    def show_role(self) -> str:
        return "Reader"
    
    @property
    def borrowed_books(self) -> int:
        return self.__borrowed_books
    
    # Add borrowed books 
    def borrow_book(self) -> None:
        self.__borrowed_books +=1
    
    # decrease total borrowed books when return a book
    def return_book(self) -> None:
        if self.__borrowed_books > 0:
            self.__borrowed_books -= 1