class Book:

    allowed_statuses = ["available", "checked out", "reserved"]

    def __init__(self, title: str, author: str, isbn: str, status: str, year: int) -> None:
        self.title = title
        self.author = author
        self.__isbn = isbn
        self.status = status 
        self.year = year
    
    def __str__(self) -> str:
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.__isbn}, status: {self.status}, Year: {self.year}"

    def __repr__(self) -> str:
        return f"<Book({self.title!r}, {self.author!r}, {self.__isbn!r}, {self.status!r}, {self.year!r})>"


    @property
    def isbn(self) -> str:
        return self.__isbn
    
    @property
    def status(self) -> str:
        return self._status

    @status.setter
    def status(self, status: str) -> None:
        if status not in Book.allowed_statuses:
            raise ValueError(f"Status must be one of {Book.allowed_statuses}")
        else:
            self._status = status