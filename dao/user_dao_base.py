from abc import ABC, abstractmethod
from models.user import User

class UserDAOBase(ABC):
    @abstractmethod
    def add_user(self, user: User): ...
    
    @abstractmethod
    def get_all_users(self) -> list[User]: ...


