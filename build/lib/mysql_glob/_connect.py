import mysql.connector
from ._logs import load_mysql_logs, load_mysql_connector_conf

def gen_mysql_server_connector():
    host, user, password = load_mysql_logs()
    use_pure, raise_on_warnings = load_mysql_connector_conf()
    c = mysql.connector.connect(host=host,
                                user=user,
                                password=password,
                                use_pure=use_pure,
                                raise_on_warnings=raise_on_warnings)
    return c
