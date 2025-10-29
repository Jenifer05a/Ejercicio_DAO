from models.user import User
from dao.user_dao_base import UserDAOBase
import os

class UserDAOTxt(UserDAOBase):
    def __init__(self, filepath: str):
        self.filepath = filepath
        if not os.path.exists(filepath):
            with open(filepath, "w") as f:
                f.write("id,name,email\n")

    def add_user(self, user: User):
        user_id = len(self.get_all_users()) + 1
        with open(self.filepath, "a") as f:
            f.write(f"{user_id},{user.name},{user.email}\n")

    def get_all_users(self) -> list[User]:
        users = []
        with open(self.filepath, "r") as f:
            next(f)
            for line in f:
                id_, name, email = line.strip().split(",")
                users.append(User(int(id_), name, email))
        return users
