from xml.etree import ElementTree as ET
from models.user import User
from dao.user_dao_base import UserDAOBase
import os

class UserDAOXML(UserDAOBase):
    def __init__(self, filepath: str):
        self.filepath = filepath
        if not os.path.exists(filepath):
            root = ET.Element("users")
            tree = ET.ElementTree(root)
            tree.write(filepath, encoding="utf-8", xml_declaration=True)

    def add_user(self, user: User):
        tree = ET.parse(self.filepath)
        root = tree.getroot()

        user_id = len(root.findall("user")) + 1
        user_el = ET.SubElement(root, "user", id=str(user_id))
        ET.SubElement(user_el, "name").text = user.name
        ET.SubElement(user_el, "email").text = user.email

        tree.write(self.filepath, encoding="utf-8", xml_declaration=True)

    def get_all_users(self) -> list[User]:
        tree = ET.parse(self.filepath)
        root = tree.getroot()
        users = []
        for user_el in root.findall("user"):
            uid = int(user_el.attrib["id"])
            name = user_el.find("name").text
            email = user_el.find("email").text
            users.append(User(uid, name, email))
        return users
