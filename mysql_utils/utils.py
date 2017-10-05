import os
import configparser

MYSQL_UTILS_PATH = os.path.dirname(os.path.abspath(__file__))
CONFIG_FULL_PATH = "{0}/m.conf.ini"

def str_listify(*a):
    if not a:
        return
    return "({0})".format(
        ''.join(
            ["`{0}`".format(a[0])] + [", `{0}`".format(i) for i in a[1::]]
        )
    )

def tuple_stringify(*t):
    targs = list(t)
    if len(targs) == 1:
        return "('{0}')".format(targs[0])
    return str(tuple(targs))

def extract_from_config_file():
    pass


def store_connector():
    def wrap_func(func):
        def wrap_args(*args, **kwargs):
            c = func(*args, **kwargs)
            return c
