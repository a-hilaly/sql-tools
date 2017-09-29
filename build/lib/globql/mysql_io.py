from ._connector import gen_mysql_server_connector

def execute_only(*args, commit=False):
    connector = None
    try:
        cursor = connector.cursor()
    except:
        raise BadConnector(connector)
    for query in list(args):
        cursor.execute(query)
    if commit:
        connector.commit()

def execute_and_fetch(*args, commit=False):
    Connector = None
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
