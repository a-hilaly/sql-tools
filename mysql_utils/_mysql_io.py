import mysql.connector


class BadConnector(Exception):
    pass


def load_mysql_logs():
    #return "192.168.1.79", "amine", "uehMLMRw"
    #return "localhost", "root", "uehMLMRw"
    return 'localhost', 'root', ''


def load_mysql_connector_conf():
    return True, True


def gmsc(host, user, password, use_pure=True, raise_on_warnings=True):
    """
    Generate Mysql Connection from params
    """
    connection = mysql.connector.connect(
        host=host, user=user, password=password,
        use_pure=use_pure, raise_on_warnings=raise_on_warnings
    )
    return connection


def generate_conf_connection():
    """
    Generate Mysql Connection from configuration file
    """
    host, user, password = load_mysql_logs()
    use_pure, raise_on_warnings = load_mysql_connector_conf()
    return gmsc(host, user, password, use_pure, raise_on_warnings)


def execute_only(*args, commit=False, connector=None):
    """
    Execute only
    """
    if connector is None:
        connector = generate_conf_connection()
    try:
        cursor = connector.cursor()
    except:
        raise BadConnector(connector)
    for query in list(args):
        cursor.execute(query)
    if commit:
        connector.commit()


def execute_and_fetch(*args, connector=None):
    """
    Excute and fetch results
    """
    if connector is None:
        connector = generate_conf_connection()
    try:
        cursor = connector.cursor()
    except:
        raise BadConnector(connector)
    for query in list(args):
        cursor.execute(query)
    result = []
    for e in cursor:
        result.append(e)
    return result
