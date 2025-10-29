import pandas as pd
from models.user import User
from dao.user_dao_base import UserDAOBase
class UserDAOExcel(UserDAOBase):
    def __init__(self, filepath):
        self.filepath = filepath
        self.columns = ["user_id", "name", "email"]

    def _create_empty_file(self):
        df = pd.DataFrame(columns=self.columns)
        df.to_excel(self.filepath, index=False)

    def get_all_users(self):
        try:
            df = pd.read_excel(self.filepath)
            return [User(row["user_id"], row["name"], row["email"]) for _, row in df.iterrows()]
        except FileNotFoundError:
            self._create_empty_file()
            return []

    def add_user(self, user):
        try:
            df = pd.read_excel(self.filepath)
        except FileNotFoundError:
            self._create_empty_file()
            df = pd.read_excel(self.filepath)

        if user.user_id is None or user.user_id == 0:
            if df.empty:
                new_id = 1
            else:
                new_id = int(df["user_id"].max()) + 1 
            user.user_id = new_id

        new_row = {"user_id": user.user_id, "name": user.name, "email": user.email}
        df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
        df.to_excel(self.filepath, index=False)



