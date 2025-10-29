class User:
    def __init__(self, user_id: int | None, name: str, email: str):
        self.user_id = user_id
        self.name = name
        self.email = email

    def __repr__(self):
        return f"User({self.user_id}, '{self.name}', '{self.email}')"
