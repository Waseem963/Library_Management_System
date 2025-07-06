from library.user_manager import UserManager
from library.reader import Reader
from library.staff import Staff


# إنشاء مدير المستخدمين
user_manager = UserManager()

# إنشاء بعض القراء والموظفين
reader1 = Reader("Ali", "R001", 2)
reader2 = Reader("Sara", "R002", 1)

staff1 = Staff("Omar", "S001", "Librarian", "Main")
staff2 = Staff("Lina", "S002", "Assistant", "Kids Section")

# اختبار دالة add_user
user_manager.add_user(reader1)
user_manager.add_user(reader2)
user_manager.add_user(staff1)
user_manager.add_user(staff2)

# اختبار دالة get_all_users
print("\n--- All users ---")
for user in user_manager.get_all_users():
    print(user)

# اختبار دالة get_readers
print("\n--- Readers ---")
for reader in user_manager.get_readers():
    print(reader)

# اختبار دالة get_staff
print("\n--- Staff ---")
for staff in user_manager.get_staff():
    print(staff)

# تسجيل إضافات كتب لموظف محدد
user_manager.record_book_addition(staff1)
user_manager.record_book_addition(staff1)
user_manager.record_book_addition(staff2)

# اختبار دالة books_by_staff
print(f"\ntotal books has been added by staff {staff1.name}: {user_manager.books_by_staff(staff1)}")
print(f"total books has been added by staff {staff2.name}: {user_manager.books_by_staff(staff2)}")

# اختبار موظف لم يُسجل له كتب
staff3 = Staff("Khaled", "S003", "Assistant", "Archive")
print(f"total books has been added by staff {staff3.name}: {user_manager.books_by_staff(staff3)}")  # لازم تطلع 0
