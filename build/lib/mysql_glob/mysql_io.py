from ._connect import gen_mysql_server_connector as GMSC

class BadConnector(Exception):
    pass

def execute_only(*args, commit=False):
    connector = GMSC()
    try:
        cursor = connector.cursor()
    except:
        raise BadConnector(connector)
    for query in list(args):
        cursor.execute(query)
    if commit:
        connector.commit()

def execute_and_fetch(*args, commit=False):
    connector = GMSC()
    result = []
    try:
        cursor = connector.cursor()
    except:
        raise BadConnector(connector)
    for query in list(args):
        cursor.execute(query)
    for e in cursor:
        result.append(e)
    if commit:
        connector.commit()
    return result
