from mysql_utils.utils import bin2str
from mysql_utils._predef_queries import (
    ADD_USER,
    DROP_USER,
    LOCK_USER,
    UNLOCK_USER,
)
from mysql_utils._mysql_io import (
    execute_only,
    execute_and_fetch,
)
from mysql_utils.mysql_queries import select_elements

_listify = lambda l : ''.join([str(l[0])] + [', {0}'.format(i) for i in l[1::]])


def create_user(user, host, password):
    """
    Add User to mysql server configuration
    """
    execute_only(ADD_USER.format(user, host, password))


def remove_user(user, host):
    """
    Remove User from mysql server configuration
    """
    execute_only(DROP_USER.format(user, host))


def users_list(filter_by=['User', 'Host', 'account_locked']):
    """
    Return list of users filtred by filtred_by + *args
    """
    s = _listify(filter_by)
    res = select_elements('mysql', 'user', selection=s)
    _res = []
    _t = []
    for elements in res:
        _t = ()
        for i in elements:
            _t += (bin2str(i), )
        _res += [_t]
    return _res


def lock_user(user, host):
    """
    Show User grants
    """
    execute_only(LOCK_USER.format(user, host))


def unlock_user(user, host):
    """
    Show User grants
    """
    execute_only(UNLOCK_USER.format(user, host))
