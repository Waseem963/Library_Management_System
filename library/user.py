from abc import ABC, abstractmethod

class User(ABC):
    """
    This class represents all users in library including stuff and readers.

    Attributes:
    name (str): User name.
    user_id:  User ID.

    Methods:
    show_role(): abstractmethod reqiures for inheretnece classes to fill it with a role
    """

    def __init__(self, name: str, user_id: str) -> None:
        self.__name = name
        self.__user_id = user_id
    
    def __str__(self) -> str:
        return f"User Name: {self.__name}, User ID: {self.__user_id}"

    def __repr__(self) -> str:
        return f"<User(User Name: {self.__name!r}, User ID: {self.__user_id!r})>"

    @property
    def name(self)-> str:
        return self.__name
    
    @property
    def user_id(self) -> str:
        return self.__user_id
    
    # Abstractmethod for all other user to identify their roles
    @abstractmethod
    def show_role(self) -> str:
        pass

