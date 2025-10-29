import pyodbc
from models.user import User
from dao.user_dao_base import UserDAOBase

class UserDAOSQLServer(UserDAOBase):
    def __init__(self, host, user, password, database, driver="ODBC Driver 17 for SQL Server"):
        self.conn = pyodbc.connect(
            f"DRIVER={{{driver}}};"
            f"SERVER={host};"
            f"DATABASE={database};"
            f"UID={user};"
            f"PWD={password};"
            f"TrustServerCertificate=yes;"
        )
        self._create_table()

    def _create_table(self):
        cursor = self.conn.cursor()
        cursor.execute("""
            IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='users' AND xtype='U')
            CREATE TABLE users (
                id INT IDENTITY(1,1) PRIMARY KEY,
                name NVARCHAR(255) NOT NULL,
                email NVARCHAR(255) UNIQUE NOT NULL
            )
        """)
        self.conn.commit()

    def add_user(self, user: User):
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO users (name, email) VALUES (?, ?)",
            (user.name, user.email)
        )
        self.conn.commit()

    def get_all_users(self) -> list[User]:
        cursor = self.conn.cursor()
        cursor.execute("SELECT id, name, email FROM users")
        rows = cursor.fetchall()
        return [User(row.id, row.name, row.email) for row in rows]


