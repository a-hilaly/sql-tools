import os
import configparser

MYSQL_UTILS_PATH = os.path.dirname(os.path.abspath(__file__))
CONFIG_FULL_PATH = "{0}/conf.ini"


def str_listify(*a, re=None):
    if not a:
        return
    if re is None:
        regex = "{0}"
    else:
        regex = re
    return "({0})".format(
        ''.join(
            [regex.format(a[0])] + [
                ", {0}".format(regex).format(i) for i in a[1::]
            ]
        )
    )


def tuple_stringify(*t):
    targs = list(t)
    if len(targs) == 1:
        return "('{0}')".format(targs[0])
    return str(tuple(targs))


def store_connector():
    def wrap_func(func):
        def wrap_args(*args, **kwargs):
            c = func(*args, **kwargs)
            return c


def bin2str(t):
    return t.decode('utf-8')


def _tuplik(e, indexes):
    """
    """
    if len(e) == 1:
        return e[0]
    else:
        R = [e[i] for i in indexes]
        if len(R) == 1:
            return R[0]
        return R


def _refetch_filter(indexes):
    """
    Matrix (2Dlist) raws [indexes]
    """
    def wrap_func(func):
        if not indexes:
            return func
        def wrap_args(*args, **kwargs):
            res = func(*args, **kwargs)
            ress = []
            for i in res:
                ress.append(_tuplik(i, indexes))
            if len(ress) == 1:
                return ress[0]
            return ress
        return wrap_args
    return wrap_func
