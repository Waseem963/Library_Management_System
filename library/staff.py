from user import User
#from library import Library 

class Staff(User):
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

    def show_role(self) -> str:
        return f"Staff"

    #def register_book(self, library: "Library", title: str, author: str, isbn: str, status: str, year: int) -> None:
        #library.add_book(title, author, isbn, status, year)
