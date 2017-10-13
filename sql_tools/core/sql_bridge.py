import mysql.connector
# import coonectors here

from sql_tools.config import get_logs

connection_map = {
    "mysql" : {"alias" : "",
               "connector" : mysql.connector,
               "config-keys" : ['raise_on_warnings', 'use_pure'],
               "default_port" : 3306},
    # add connectors here
    "mango" : {"" : ""},
    "sql" : {"" : ""},
    "maria" : {"" : ""},
}

__credentials__ = ('host', 'port', 'user', 'password')

class UnexpectedArguments(Exception):
    def __init__(self):
        Exception.__init__(self, "Unexpected arguments style")

class SQLBridge(object):

    __slots__ = ['_system',
                 '_host',
                 '_port',
                 '_user',
                 '_password',
                 '_connector',
                 '_connected',
                 '_status',
                 '_config']

    @property
    def connector(self):
        # Return MySQL Actual connector
        return self._connector

    @property
    def cursor(self):
        # Return MySQL Actual connector's cursor
        return self._connector.cursor()

    @property
    def status(self):
        return self._status

    @property
    def credentials(self):
        print("""{0} CREDENTIALS
         - host : {1}
         - port : {2}
         - user : {3}
         - password : {4}
         - config : {5}""".format(self._system.upper(), *self._credentials))


    def __init__(self, system):
        self._system = system
        self._host = None
        self._port = None
        self._user = None
        self._password = None
        self._config = {}
        self._connector = None
        self._connected = False
        self._status = 1

    def _credentials(self, exclude_nulls=False):
        if not exclude_nulls:
            return {"host" : self._host,
                    "port" : self._port,
                    "user" : self._user,
                    "password" : self._password,
                    **self._config}

        ncred = {}
        for cred, val in self._credentials(exclude_nulls=False).items():
            if val:
                ncred[cred] = val
        return ncred

    def _load_system_configuration(self):
        data = get_logs(self._system)
        for cred in list(data.keys()):
            if cred in __credentials__:
                setattr(self, '_' + cred, data[cred])
            else:
                self._config[cred] = data[cred]
        if not self._port:
            self._port = connection_map[self._system]['default_port']

    def _make_connection(self):
        connector = connection_map[self._system]['connector']
        kws = self._credentials(exclude_nulls=True)
        cnx = connector.connect(**kws)
        self._connector = cnx

    def connect(self, init=False):
        # Class connection
        if init:
            self._make_connection()
        else:
            self._connector.connect()
        self._status = 0
        self._connected = True

    def commit(self):
        # commit
        self._connector.commit()

    def disconnect(self):
        # Class disconnection
        self._connector.close()
        self._status = 1
        self._connected = False
