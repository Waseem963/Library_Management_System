class Book:
    """
    This class represents book object.

    Attributes:
    allowed_statuses (List): allowed statuses that the user can use to represent books status.
    title (str): Name of the book.
    author (str): Who wrote the book.
    isbn (str): Unique number represents the book.
    status (str): status of the book (available, checked out, etc..)
    year (int): When the book has been publiched.

    Methods:
    status() (setter): to add a specific status to the book.


    """
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

    # Add a specific status to the book
    @status.setter
    def status(self, status: str) -> None:
        status = status.lower()
        if status not in Book.allowed_statuses:
            raise ValueError(f"Status must be one of {Book.allowed_statuses}")
        else:
            self._status = status