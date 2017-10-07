import mysql.connector as MSCN

class UnexpectedArguments(Exception):
    def __init__(self, args_number):
        Exception.__init__(
            self, "Unexpected number of arguments : {0}".format(args_number)
        )

class MySQLConnection(object):

    __slots__ = ['_host', '_user', '_password', '_password', '_connector',
                 '_connected', '_status', '_use_pure', '_raise_on_warnings']

    @property
    def connector(self):
        # Return MySQL Actual connector
        return self._connector

    @property
    def cursor(self):
        # Return MySQL Actual connector's cursor
        return self._connector.cursor()

    def __init__(self, *args, **kwargs):
        self._host = None
        self._user = None
        self._password = None
        self._use_pure = False
        self._raise_on_warnings = False
        self._connector = None
        self._connected = False
        self._status = 1
        #####____________________________________________________#####
        if args or kwargs:
            l = list(args) + list(kwargs.values())
            if len(l) != 5:
                raise UnexpectedArguments(l)
            else:
                self.load(*args, **kwargs)
                self.connect(True)

    def load(self, host=None, user=None, password=None, use_pure=None,
             raise_on_warnings=None):
        # Load mysql connector arguments
        self._host = host
        self._user = user
        self._password = password
        self._use_pure = use_pure
        self._raise_on_warnings = raise_on_warnings

    def _connect(self):
        # Make connection
        cnx = MSCN.connect(host=self._host,
                           user=self._user,
                           password=self._password,
                           use_pure=self._use_pure,
                           raise_on_warnings=self._raise_on_warnings)
        self._connector = cnx

    def connect(self, use_logs=False):
        # Class connection
        if use_logs:
            self._connect()
        else:
            self._connector.connect()
        self._status = 0
        self._connected = True

    def commit(self):
        self._connector.commit()

    def disconnect(self):
        # Class disconnection
        self._connector.close()
        self._status = 1
        self._connected = False

def logit(**logs):
    return MySQLConnection(**logs)
