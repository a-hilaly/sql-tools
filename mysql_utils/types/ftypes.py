from .mysql_types import Mysql_Type

_type = lambda obj : obj.__class__.__name__
_listify = lambda l : ''.join([str(l[0])] + [', {0}'.format(i) for i in l[1::]])

NOT_NULL = " NOT NULL"
DEFAULT = " DEFAULT {0}"
DEFAULT_STR = " DEFAULT '{0}'"
AUTO_INCREMENT = " AUTO_INCREMENT"
ON_UPDATE = " ON UPDATE {0}"
CURRENT_TIMESTAMP =  "CURRENT_TIMESTAMP"


class INT(Mysql_Type):

    __slots__ = ['_type', '_init',
                 '_size', '_not_null', '_default', '_auto_incr']

    def __init__(self, size=None, not_null=False, default=None,
                 auto_increment=False):
        if default and auto_increment:
            raise Exception()

        Mysql_Type.__init__(self, _type(self))
        self._init = True
        self._size = size
        self._not_null = not_null
        self._default = default
        self._auto_incr = auto_increment

    def _printf(self):
        v = "{0}{1}".format(self._type, '({0})'.format(self._size))
        if self._not_null:
            v += NOT_NULL
        if self._default != None:
            v += DEFAULT.format(self._default)
        elif self._auto_incr:
            v += AUTO_INCREMENT
        return v


class VARCHAR(Mysql_Type):

    __slots__ = ['_type', '_init', '_size', '_not_null', '_default']

    def __init__(self, size=None, not_null=False, default=None):
        Mysql_Type.__init__(self, _type(self))
        self._init = True
        self._size = size
        self._not_null = not_null
        self._default = default

    def _printf(self):
        v = "{0}{1}".format(self._type, '({0})'.format(self._size))
        if self._not_null:
            v += NOT_NULL
        if self._default != None:
            v += DEFAULT_STR.format(self._default)
        return v


class BOOLEAN(Mysql_Type):

    __slots__ = ['_type', '_init', '_not_null', '_default']

    def __init__(self, not_null=False, default=None):
        Mysql_Type.__init__(self, _type(self))
        self._init = True
        self._not_null = not_null
        self._default = default

    def _printf(self):
        v = "{0}".format(self._type)
        if self._not_null:
            v += NOT_NULL
        if self._default != None:
            v += DEFAULT.format(self._default)
        return v


class ENUM(Mysql_Type):

    __slots__ = ['_type', '_init', '_enum_ct', '_default']

    def __init__(self, enum_ct=None, default=None):
        Mysql_Type.__init__(self, _type(self))
        self._init = True
        self._enum_ct = enum_ct
        self._default = default

    def _printf(self):
        v = "{0}".format(self._type)
        v += "({0})".format(_listify(self._enum_ct))
        if self._default:
            if isinstance(self._default, str):
                v += DEFAULT_STR.format(self._default)
            else:
                v += DEFAULT.format(self._default)
        return v


class JSON(Mysql_Type):

    __slots__ = ['_type', '_init', '_default']

    def __init__(self, default=None):
        Mysql_Type.__init__(self, _type(self))
        self._init = True
        self._default = default

    def _printf(self):
        v = "{0}".format(self._type)
        if self._default != None:
            v += DEFAULT_STR.format(self._default.__str__())
        return v


class TIMESTAMP(Mysql_Type):

    __slots__ = ['_type', '_init', '_default', '_on_update']

    def __init__(self, default=False, on_update=False):
        Mysql_Type.__init__(self, _type(self))
        self._init = True
        self._default = default
        self._on_update = on_update

    def _printf(self):
        v = "{0}".format(self._type)
        if self._default == 'NOW':
            v += DEFAULT.format(CURRENT_TIMESTAMP)
        if self._on_update == 'NOW':
            v += ON_UPDATE.format(CURRENT_TIMESTAMP)
        return v
