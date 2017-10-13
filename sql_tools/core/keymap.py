from sql_tools.utils import str_listify, tuple_stringify


#MYSQL VU

_VERSION = "select version();"
_USER = "select user();"

# Databases querries [SHOW | CREATE | DELETE | USE]

_SHOW_DATABASES = "SHOW DATABASES;"
_CREATE_DATABASE = "CREATE DATABASE {0};"
_DELETE_DATABASE = "DROP DATABASE {0};"
_USE_DATABASE = "USE {0};"

# Table querries [ SHOW | DESC | CREATE | DELETE ]

_TABLE_FIELDS = "DESC {0}.{1};"
_SHOW_TABLES = "SHOW TABLES IN {0};"
_CREATE_TABLE = """CREATE TABLE {0}.{1} (
{2}
) ENGINE=InnoDB DEFAULT CHARSET=latin1;"""
_DELETE_TABLE = "DROP TABLE {0}.{1};"
# Autoincr
_AUTOINCR = "ALTER TABLE {0}.{1} AUTO_INCREMENT = {2};"
#copy table
_CREATE_TABLE_LIKE = "CREATE TABLE {0}.{1} LIKE {0}.{2};"
_INSERT_TABLE_CONTENT = "INSERT INTO {0}.{1} SELECT * FROM {0}.{2};"

#COLUMNS [ ADD | DELETE | CHANGE ]

_ADD_COLUMN = """ALTER TABLE {0}.{1}
ADD {2} {3};"""
_DELETE_COLUMN = """ALTER TABLE {0}.{1}
DROP COLUMN {2};"""
_CHANGE_COLUMN = """ALTER TABLE {0}.{1}
CHANGE {2} {3} {4};"""

# Data [ INSERT | INSERT_OPT | DELETE  | UPDATE]

_INSERT_VALUE_NO_MATCH = """INSERT INTO {0}.{1}
VALUES {2};"""
_INSERT_VALUE_WK = """INSERT INTO {0}.{1}
{2}
VALUES {3};"""
_DELETE_VALUES = """DELETE FROM {0}.{1}
WHERE {2}"""
_UPDATE_ELEMENT = """UPDATE {0}.{1}
SET {2}
WHERE {3}"""

# Selection [ SELECT* | SELECT | SELECT_WITHSORT | OPT ]

_SELECT_TABLE = "SELECT * FROM {0}.{1};"
_SELECT_GENERAL = """SELECT {0}
FROM {1}.{2}
"""
_SORTED_TABLE = """SELECT {0}
FROM {1}.{2}
ORDER BY {3} {4}
"""
_SELECT_OPTI = """SELECT {0}
FROM {1}.{2}
ORDER BY {3} {4}
LIMIT {5}"""

## Users [ CREATE | DROP | LOCK | UNLOCK ]

ADD_USER = "CREATE USER '{0}'@'{1}' IDENTIFIED BY '{2}';"
DROP_USER = "DROP USER '{0}'@'{1}';"
UNLOCK_USER = "ALTER USER '{0}'@'{1}' ACCOUNT UNLOCK;"
LOCK_USER = "ALTER USER '{0}'@'{1}' ACCOUNT LOCK;"

# Users Grants [ GRANT | REVOKE | SHOW ]

GRANT_POWER = "GRANT {0} ON {1}.{2} TO '{3}'@'{4}';"
REVOKE_POWER = "REVOKE {0} ON {1}.{2} FROM '{3}'@'{4}';"
USER_GRANTS = "SHOW GRANTS FOR '{0}'@'{1}';"


# Querries constructors

def fieldify(a, b, comma=True, new_line=True):
    """
    Table creation fields type generator
    """
    txt = None
    if "primary_key" in str(a):
        txt = "  PRIMARY KEY (`{0}`)".format(b) + "{0}"
    elif "unique_key" == a:
        txt = "  UNIQUE KEY (`{0}`)".format(b) + "{0}"
    else:
        txt = "  `{0}` {1}".format(a, b) + "{0}"

    if comma and new_line:
        return txt.format(",\n")
    elif comma and not new_line:
        return txt.format(",")
    elif (not comma) and new_line:
        return txt.format("\n")
    else:
        return txt.format("")


def _CT_QUERY(db=None, table=None, **kwargs):
    """
    Create Table query genertor
    """
    n = len(kwargs)
    count = n
    comma = True
    new_line=True
    m = ""
    for field, _type in kwargs.items():
        if count < 2:
            comma = False
            new_line = False
        m += fieldify(field, _type, comma=comma, new_line=new_line)
        count -= 1
    return _CREATE_TABLE.format(db, table, m)


def _IE_QUERY(db, table, **kwargs):
    """
    Insert Element Query
    """
    kwa = str_listify(*kwargs.keys(), re='`{0}`')
    rgs = tuple_stringify(*list(kwargs.values()))
    return _INSERT_VALUE_WK.format(db, table, kwa, rgs)


def _DL_QUERY(db, table, w, lim):
    """
    Delete element query
    """
    res = _DELETE_VALUES.format(db, table, w)
    if lim > 0:
        return res + "\n LIMIT {0};".format(lim)
    return res + ";"


def _SL_QUERY(db, table, w, lim, s):
    """
    Select element query
    """
    res = _SELECT_GENERAL.format(s, db, table)
    if w:
        res = res + "\n WHERE {0}".format(w)
    if lim > 0:
        return res + "\n LIMIT {0};".format(lim)
    return res + ";"


def _UE_QUERY(db, table, w, lim, s):
    """
    Update Element query
    """
    res = _UPDATE_ELEMENT.format(db, table, s, w)
    if lim > 0:
        return res + "\n LIMIT {0};".format(lim)
    return res + ";"
