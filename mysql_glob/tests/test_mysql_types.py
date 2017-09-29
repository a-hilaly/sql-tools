from mysql_glob._mysql_types import (Mysql_Type,
                                     INT,
                                     VARCHAR,
                                     BOOLEAN,
                                     ENUM,
                                     JSON,
                                     TIMESTAMP)


def test_mysql_type_basics():
    T = Mysql_Type('int')
    assert T._type == 'int'
    assert T._init is None
    try:
        Mysql_Type.decode(T)
    except NotImplemented:
        pass


def test_mysql_types_minimal_kwargs():
    i, v, b = INT(10), VARCHAR(10), BOOLEAN()
    e, j, t = ENUM([1, 2]), JSON(), TIMESTAMP()
    assert Mysql_Type.eval(i) == 'INT(10)'
    assert Mysql_Type.eval(v) == 'VARCHAR(10)'
    assert Mysql_Type.eval(b) == 'BOOLEAN'
    assert Mysql_Type.eval(e) == 'ENUM(1, 2)'
    assert Mysql_Type.eval(j) == 'JSON'
    assert Mysql_Type.eval(t) == 'TIMESTAMP'


def test_mysql_types_default():
    i, v, b = INT(10, default=15), VARCHAR(10, default='A'), BOOLEAN(default=0)
    e, j = ENUM([1, 2], default=2), JSON(default=[1, 5, {1 : 3}])
    t = TIMESTAMP(default='NOW')
    assert Mysql_Type.eval(i) == 'INT(10) DEFAULT 15'
    assert Mysql_Type.eval(v) == "VARCHAR(10) DEFAULT 'A'"
    assert Mysql_Type.eval(b) == 'BOOLEAN DEFAULT 0'
    assert Mysql_Type.eval(e) == 'ENUM(1, 2) DEFAULT 2'
    assert Mysql_Type.eval(j) == "JSON DEFAULT '[1, 5, {1 : 3}]'"
    assert Mysql_Type.eval(t) == 'TIMESTAMP DEFAULT CURRENT_TIMESTAMP'

def test_mysql_types_not_null():
    i, v, b = INT(10, True), VARCHAR(10, not_null=True), BOOLEAN(1)
    assert Mysql_Type.eval(i) == 'INT(10) NOT NULL'
    assert Mysql_Type.eval(v) == "VARCHAR(10) NOT NULL"
    assert Mysql_Type.eval(b) == 'BOOLEAN NOT NULL'

def test_mysql_object_max_cases():
    try:
        i = INT(10, True, 15, True)
    except Exception:
        pass
    i = INT(10, True, auto_incr=True)
    v = VARCHAR(10, True, default='A')
    b = BOOLEAN(not_null=True, default=1)
    t = TIMESTAMP(True, True)
    assert Mysql_Type.eval(i) == 'INT(10) NOT NULL AUTO_INCREMENT'
    assert Mysql_Type.eval(v) == "VARCHAR(10) NOT NULL DEFAULT 'A'"
    assert Mysql_Type.eval(b) == 'BOOLEAN NOT NULL DEFAULT 1'
    assert Mysql_Type.eval(t) == """TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        ON UPDATE CURRENT_TIMESTAMP"""

__all__ = [test_mysql_type_basics,
           test_mysql_types_minimal_kwargs,
           test_mysql_types_default,
           test_mysql_types_not_null,
           test_mysql_object_max_cases]
