from library.library_system import Library
from library.user_manager import UserManager
from library.reader import Reader
from library.staff import Staff
from library.statistics import Statistics


# Create a library
library = Library()

# Create user manager
user_manager = UserManager()

# Create statistics
statistics = Statistics(library, user_manager)



# Create some Readers
reader1 = Reader("Ali", "R001", 2)
reader2 = Reader("Sara", "R002", 1)

# Create some Staff
staff1 = Staff("Omar", "S001", "Librarian", "Main")
staff2 = Staff("Lina", "S002", "Assistant", "Kids Section")
staff3 = Staff("Khaled", "S003", "Assistant", "Archive")

# Add users to user manager
user_manager.add_user(reader1)
user_manager.add_user(reader2)
user_manager.add_user(staff1)
user_manager.add_user(staff2)
user_manager.add_user(staff3)


# Staff add books in the library
staff1.register_book(library, "Became a professional Python programmer in 10 minutes", "Karim", "1554321", "Available", 2020)
user_manager.record_book_addition(staff1)
staff1.register_book(library, "Became a professional C programmer in 10 minutes", "Adam", "144241", "checked out", 2019)
user_manager.record_book_addition(staff1)
staff2.register_book(library, "Became a professional C++ programmer in 10 minutes", "Ullis", "1351721", "Available", 2023)
user_manager.record_book_addition(staff2)
staff2.register_book(library, "Became a professional Assembly programmer in 10 minutes", "Kevin", "1114121", "reserved", 2021)
user_manager.record_book_addition(staff2)



# Get all users
print("\n--- All users ---")
for user in user_manager.get_all_users():
    print(user)

# Get all readers
print("\n--- Readers ---")
for reader in user_manager.get_readers():
    print(reader)
  

# Get all staff
print("\n--- Staff ---")
for staff in user_manager.get_staff():
    print(staff)
    
# Get total readers and staff
count_reader = len(user_manager.get_readers())
count_staff = len(user_manager.get_staff())
print(f"\nThere are {count_reader} readers and {count_staff} staff in the library\n")

# Get all books in the library
count_books = 0
for book in library.books:
    count_books += 1
    print(f"Book: {book}")

# Get total books in the library
print(f"\nThere are {count_books} books in the library")

# books_by_staff
print(f"\nTotal books has been added by staff {staff1.name}: {user_manager.books_by_staff(staff1)}")
print(f"Total books has been added by staff {staff2.name}: {user_manager.books_by_staff(staff2)}")

# A staff that did not add any books yet
print(f"total books has been added by staff {staff3.name}: {user_manager.books_by_staff(staff3)}")

try:
# Search a book that is exist in the library
    print(f"\nYou searched about a book: {library.search_book("1554321")}")

    # Search a book that is not in the library
    print(library.search_book("9988"))
except LookupError as e:
    print(e)


# Try to add a book that is already in the library
try:
    staff2.register_book(library, "Became a professional Assembly programmer in 10 minutes", "Kevin", "1114121", "reserved", 2021)

except ValueError as e:
    print(e)

try:
    # Remove a book exist in the library
    print(library.remove_book("1114121"))

    #remove a book does not exist in the library
    print(library.remove_book("1"))
    
except LookupError as e:
    print(e)