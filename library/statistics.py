from library_system import Library
from reader import Reader
from staff import Staff

class Statistics:
    """
    This class represents library's statistics for books and users.

    Attributes:
    library (Library): library class to get books objects.
    staff (Staff): represents staff users in the library.

    Methods:
    total_books(): Return total books in the library (rented, available, etc..).
    available_books(): Return available books in the library.
    checked_out_books(): Return check out books.
    reserved_books(): Return reserved books.
    users_count(): Return how many users the library has (staff, readers).
    books_by_staff(): Return how many books has been added by a staff.

    """

    def __init__(self) -> None:
        self.library = Library()
        self.staff = Staff
    
    # Show total books in the library for all its status
    def total_books(self) -> int:
        return len(self.library.books)
    
    # Show available books in the library
    def available_books(self) -> int:
        available_books = [book for book in self.library.books if book.status == "available"]
        return len(available_books)
    
    # Show checked out books in the library
    def checked_out_books(self) -> int:
        checked_out_books = [book for book in self.library.books if book.status == "checked out"]
        return len(checked_out_books)
    
    # Show reserved books in the library
    def reserved_books(self) -> int:
        reserved_books = [book for book in self.library.books if book.status == "reserved_books"]
        return len(reserved_books)

    # Return total users in the library (readers, staff)
    # def users_count(self) -> int:
    #     readers = [reader for reader in self.library.books if isinstance(reader, Reader)]
    #     staff = [staff for staff in self.library.books if isinstance(staff, Staff)]
    #     return len(readers) + len(staff)

    # Return how many books a staff added to the library
    # def books_by_staff(self, staff: Staff) -> int:
    #     count = 0
    #     for book in self.library.books:
    #         if hasattr(book, 'added_by') and book.added_by == staff.name:
    #             count += 1
    #     return count

