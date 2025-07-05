from user import User

class Reader(User):

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

b = Reader("ali", "3333", "2")

print(b)