from abc import ABC, abstractmethod

class User(ABC):

    def __init__(self, name: str, user_id: str):
        self.__name = name
        self.__user_id = user_id

    def __str__(self):
        return f"User Name: {self.__name}, User ID: {self.__user_id}"
    
    @abstractmethod
    def show_role(self, role_type: str) -> str:
        pass
