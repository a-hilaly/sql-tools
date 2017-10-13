from .sql_io import SQLio
from sql_tools.utils import refetch_filter, listify, kwgs, bin2str
from .keymap import (
    ADD_USER,
    DROP_USER,
    LOCK_USER,
    UNLOCK_USER,
    GRANT_POWER,
    REVOKE_POWER,
    USER_GRANTS
)

try:
    SQ = SQLio('mysql')
except:
    SQ = None


##@@ USERS


def create_user(user, host, password):
    """
    Add User to mysql server configuration
    """
    SQ.execute_only(ADD_USER.format(user, host, password))


def remove_user(user, host):
    """
    Remove User from mysql server configuration
    """
    SQ.execute_only(DROP_USER.format(user, host))


def users_list(filter_by=['User', 'Host', 'account_locked']):
    """
    Return list of users filtred by filtred_by + *args
    """
    from .queries import select_elements
    s = listify(filter_by)
    res = select_elements('mysql', 'user', selection=s)
    if isinstance(res[0][0], str):
        return res
    _res = []
    _t = []
    for elements in res:
        _t = ()
        for i in elements:
            if isinstance(i, str):
                _t += (i, )
                continue
            _t += (bin2str(i), )
        _res += [_t]
    return _res


##@@ LOCKS


def lock_user(user, host):
    """
    Show User grants
    """
    SQ.execute_only(LOCK_USER.format(user, host))


def unlock_user(user, host):
    """
    Show User grants
    """
    SQ.execute_only(UNLOCK_USER.format(user, host))


##@@ GRANTS


def set_user_grants(user, host, grants=None, database=None, table=None):
    """
    Grants rights to user
    """
    g, d, t = kwgs(grants, database, table)
    SQ.execute_only(GRANT_POWER.format(g, d, t, user, host))


def revoke_user_grants(user, host, grants=None, database=None, table=None):
    """
    Revoke rights
    """
    g, d, t = kwgs(grants, database, table)
    SQ.execute_only(REVOKE_POWER.format(g, d, t, user, host))


@refetch_filter([0])
def user_grants(user, host):
    """
    Show User grants
    """
    return SQ.execute_and_fetch(USER_GRANTS.format(user, host))
