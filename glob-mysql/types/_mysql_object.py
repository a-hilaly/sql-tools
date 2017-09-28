

class s(object):
    """
    """
    @property
    def size(self):
        return self._size
    
    @property
    def default(self):
        return self._default

    @property
    def is_null(self):
        return self._is_null

    def __init__(self, t, size=None, default=None, is_null=False):
        self._type = t
        self._size = size
        self._default = default
        self._is_null = is_null

    def printf(self):
        v = "{0}{1}"
        if self._size < 0:
            v = v.format(self._type, '')
        else:
            v = v.format(self._type, '({0})'.format(self._size))
        if not self._is_null:
            v += " NOT NULL"
        if self._default:
            v += " DEFAULT {0}"
            v = v.format(self._default)
        return v
