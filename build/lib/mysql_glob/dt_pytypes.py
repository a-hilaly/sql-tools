class Mysql_Type(object):
    """
    """
    @classmethod:
    def clsname(cls):
        return cls.__class__.__name__

    @property
    def size(self):
        return self._size

    @property
    def default(self):
        return self._default

    @property
    def is_null(self):
        return self._is_null

    def __init__(self, t, size=None, default=None, not_null=False, auto_increment=False):
        self._type = t
        self._size = size
        self._default = default
        self._not_null = not_null
        self._auto_increment = auto_increment

    def printf(self):
        v = "{0}{1}"
        if self._size < 0:
            v = v.format(self._type, '')
        else:
            v = v.format(self._type, '({0})'.format(self._size))
        if self._not_null:
            v += " NOT NULL"
        if self._default:
            v += " DEFAULT {0}"
            v = v.format(self._default)
        if self._auto_increment:
            v += " AUTO_INCREMENT"
        return v

class INT(Mysql_Type):
    def __init__(self, **kwargs):
        Mysql_Type.__init__(self, self.clsname(), **kwargs)
