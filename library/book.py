class Book:
    allowed_statuses = ["available", "checked out", "reserved"]
    def __init__(self, title: str, author: str, isbn: str, status: str, year: int):
        self.title = title
        self.author = author
        self.__isbn = isbn
        self.status = status # Using the setter to validate status
        self.year = year
    
    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.__isbn}, status: {self.status}, Year: {self.year}"

    def __repr__(self):
        return f"<Book({self.title!r}, {self.author!r}, {self.__isbn!r}, {self.status!r}, {self.year!r})>" 
    

    @property
    def isbn(self):
        return self.__isbn
    
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status: str):
        if status not in Book.allowed_statuses:
            raise ValueError(f"Status must be one of {Book.allowed_statuses}")
        else:
            self._status = status