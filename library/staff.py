from library.user import User
from library.library_system import Library 

class Staff(User):
    """
    This class represents staff users in the library with thier position, department, user_id and name.

    Attributes:
    super().__init__(name, user_id) (str, str): inheretence attributes from User class (name, user_id).
    position (str): represents staff position in the library (librarian, archivist, etc..).
    department (str): represents department in the library (Circulation, Reference, etc..).

    Methods:
    show_role(): Return user role (staff).
    register_book(): register books by staff.

    """
    def __init__(self, name: str, user_id: str, position: str, department: str) -> None:
        super().__init__(name, user_id)
        self.__position = position
        self.__department = department
    
    def __str__(self) -> str:
        return f"Name: {self.name}, User ID: {self.user_id}, Position: {self.position}, Department: {self.department}"
    
    def __repr__(self) -> str:
        return f"<Staff(Name: {self.name!r}, User ID: {self.user_id!r}, Position: {self.position!r})>"

    @property
    def position(self) -> str:
        return self.__position
    
    @property
    def department(self)-> str:
        return self.__department

    # Show user role (staff)
    def show_role(self) -> str:
        return f"Staff"

    # register books in the library.
    def register_book(self, library: "Library", title: str, author: str, isbn: str, status: str, year: int) -> None:
            library.add_book(title, author, isbn, status, year)
            print( f"Staff {self.name} registered book '{title}' successfully.") 
