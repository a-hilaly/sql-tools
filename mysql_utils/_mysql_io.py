from .settings import conflogs
from ._mysql_connection import logit

CNX = logit(**conflogs())


def execute_only(*args, commit=False):
    """
    Execute only
    """
    CNX.connect()
    cursor = CNX.cursor
    for query in list(args):
        cursor.execute(query)
    if commit:
        CNX.commit()
    CNX.disconnect()



def execute_and_fetch(*args, connector=None):
    """
    Excute and fetch results
    """
    CNX.connect()
    cursor = CNX.cursor
    for query in list(args):
        cursor.execute(query)
    result = []
    for e in cursor:
        result.append(e)
    CNX.disconnect
    return result
