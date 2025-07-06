from library_system import Library
from user import User

class Statistics:
    def __init__(self) -> None:
        self.library = Library()
        self.users = User()
    
    def total_books(self) -> int:
        return len(self.library.books)
    

print(Statistics.total_books())