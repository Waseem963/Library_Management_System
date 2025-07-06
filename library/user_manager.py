from library.user import User
from library.staff import Staff
from library.reader import Reader


class UserManager:
    """
    This class manage users in the system.

    Attributes:
    users (list): represents all users in the system (staff, readers).
    staff_books (dictionary): total books a staff added to the library.

    Methods:
    add_user(): Add users to a list.
    get_all_users(): Print all users (staff, readers).
    get_readers(): Print all readers users.
    get_staff(): Print all staff users.
    record_book_addition(): Count how many book a staff added.
    books_by_staff(): Print total books added by a staff.

    """

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