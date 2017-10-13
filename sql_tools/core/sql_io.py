from .sql_bridge import SQLBridge


class SQLio(object):

    def __init__(self, system):
        self.CNX = SQLBridge(system)
        self.CNX._load_system_configuration()
        self.CNX._make_connection()

    def execute_only(self, *args, commit=False):
        """
        Execute only
        """
        self.CNX.connect()
        cursor = self.CNX.cursor
        for query in list(args):
            cursor.execute(query)
        if commit:
            self.CNX.commit()
        self.CNX.disconnect()

    def execute_and_fetch(self, *args, commit=False, connector=None):
        """
        Excute and fetch results
        """
        self.CNX.connect()
        cursor = self.CNX.cursor
        for query in list(args):
            cursor.execute(query)
        result = []
        for e in cursor:
            result.append(e)
        self.CNX.disconnect()
        return result

    @classmethod
    def Execute_only(*args, connector=None, **kwargs):
        obj = object.__new__(cls)
        obj = object.__init__(connector=connector)
        obj.execute_only(*args, **kwargs)

    @classmethod
    def Execute_and_fetch(*args, connector=None, **kwargs):
        obj = object.__new__(cls)
        obj = object.__init__(connector=connector)
        return obj.execute_and_fetch(*args, **kwargs)
