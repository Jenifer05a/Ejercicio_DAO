import json
from dao.user_dao_mysql import UserDAOMySQL
from dao.user_dao_txt import UserDAOTxt
from dao.user_dao_xml import UserDAOXML
from dao.user_dao_sql_server import UserDAOSQLServer
from dao.user_dao_excel import UserDAOExcel

def get_dao_from_config(config_path="config.json"):
    with open(config_path, "r") as f:
        config = json.load(f)

    dao_type = config["dao_type"].lower()

    if dao_type == "mysql":
        mysql_conf = config["mysql"]
        return UserDAOMySQL(
            host=mysql_conf["host"],
            user=mysql_conf["user"],
            password=mysql_conf["password"],
            database=mysql_conf["database"]
        )

    elif dao_type == "txt":
        return UserDAOTxt(config["txt"]["filepath"])

    elif dao_type == "xml":
        return UserDAOXML(config["xml"]["filepath"])
    
    elif dao_type == "sqlserver": 
        sqlserver_conf = config["sqlserver"]
        return UserDAOSQLServer(
            host=sqlserver_conf["server"],
            user=sqlserver_conf["username"],
            password=sqlserver_conf["password"],
            database=sqlserver_conf["database"]
        )
    elif dao_type == "excel":
        excel_conf = config["excel"]
        return UserDAOExcel(excel_conf["filepath"])
    else:
        raise ValueError(f"Tipo de DAO desconocido: {dao_type}")