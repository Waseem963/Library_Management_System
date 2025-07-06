from library.user import User
from library.staff import Staff
from library.reader import Reader


class UserManager:
    def __init__(self) -> None:
        self.__users = []
        self.__staff_books = {}

    def add_user(self, user: User) -> None:
        self.__users.append(user)
    
    def get_all_users(self) -> list:
        return self.__users
    
    def get_readers(self) -> list:
        return [user for user in self.__users if isinstance(user, Reader)]

    def get_staff(self) -> list:
        return [user for user in self.__users if isinstance(user, Staff)]
    
    def record_book_addition(self, staff: Staff) -> None:
        if staff.user_id in self.__staff_books:
            self.__staff_books[staff.user_id] += 1
        else:
            self.__staff_books[staff.user_id] = 1

    def books_by_staff(self, staff: Staff) -> int:
        return self.__staff_books.get(staff.user_id, 0)