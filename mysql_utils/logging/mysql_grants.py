from mysql_utils._mysql_io import execute_only, execute_and_fetch
from mysql_utils._predef_queries import GRANT_POWER, REVOKE_POWER, USER_GRANTS


def __kwgs(grants=None, on_db=None, on_tb=None):
    g, d, t = grants, on_db, on_tb
    if grants == "*":
        g = "ALL PRIVILEGES"
    if not on_db:
        d = "*"
    if not on_tb:
        t = "*"
    return g, d, t


def set_user_grants(user, host, grants=None, database=None, table=None):
    """
    Grants rights to user
    """
    g, d, t = __kwgs(grants, database, table)
    execute_only(GRANT_POWER.format(g, d, t, user, host))


def revoke_user_grants(user, host, grants=None, database=None, table=None):
    """
    Revoke rights
    """
    g, d, t = __kwgs(grants, database, table)
    execute_only(REVOKE_POWER.format(g, d, t, user, host))


def user_grants(user, host):
    """
    Show User grants
    """
    return execute_and_fetch(USER_GRANTS.format(user, host))
