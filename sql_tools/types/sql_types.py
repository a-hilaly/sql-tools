#

TYPES = [('int', 'INT'),
         ('varchar', 'VARCHAR'),
         ('boolean', 'BOOLEAN'),
         ('json', 'JSON'),
         ('timestamp', 'TIMESTAMP'),
         ('enum', 'ENUM')]

class UnknownType(Exception):
    pass

class NotImplementeD(Exception):
    pass


class SQLTypes(object):

    __slots__ = ['_type', '_init']

    def __new__(cls, *args, **kwargs):
        nm = cls.__name__
        is_type = True in [nm in e for e in TYPES] + [nm == 'SQLTypes']
        if not is_type:
            raise UnknownType()
        obj = object.__new__(cls)
        obj.__init__(*args, **kwargs)
        return obj

    def __init__(self, t):
        self._type = t
        self._init = None

    def __str__(self):
        return self._printf()

    __repr__ = __str__

    @classmethod
    def decode(cls, obj):
        if not isinstance(obj, cls):
            raise Exception()
        return obj.printf

    def _printf(self):
        """
        """
        raise NotImplementeD()

    @staticmethod
    def eval(obj):
        return obj.printf

    @property
    def printf(self):
        return self._printf()
