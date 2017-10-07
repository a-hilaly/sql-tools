from ._mysql_io import (
    execute_only,
    execute_and_fetch
)

from ._predef_queries import (
    _VERSION,
    _USER,
    _USE_DATABASE,
    _SHOW_DATABASES,
    _CREATE_DATABASE,
    _DELETE_DATABASE,
    _SHOW_TABLES,
    _TABLE_FIELDS,
    _CREATE_TABLE,
    _SELECT_TABLE,
    _USE_DATABASE,
    _DELETE_TABLE,
    _IE_QUERY,
    _DL_QUERY,
    _SL_QUERY,
    _CT_QUERY,
    _UE_QUERY,
    _AUTOINCR,
    _ADD_COLUMN,
    _DELETE_COLUMN,
    _CHANGE_COLUMN,
    _SELECT_OPTI,
)

from .types.mysql_types import Mysql_Type
from .utils import _refetch_filter


@_refetch_filter([0])
def version():
    """
    Return actual MySQL version
    """
    return execute_and_fetch(_VERSION)


@_refetch_filter([0])
def user():
    """
    Return MySQL user
    """
    return execute_and_fetch(_USER)


@_refetch_filter([0])
def databases():
    """
    Return list of all databases
    """
    return execute_and_fetch(_SHOW_DATABASES)


def make_database(db):
    """
    Create database
    """
    execute_only(_CREATE_DATABASE.format(db))


def remove_database(db):
    """
    Drop database
    """
    execute_only(_DELETE_DATABASE.format(db))


def use_database(db): #XXX: Maybe is useless
    """
    Use database
    """
    pass


@_refetch_filter([0])
def tables(db):
    """
    """
    return execute_and_fetch(_SHOW_TABLES.format(db))


@_refetch_filter([0])
def table_fields(db, table):
    """
    Return a list of table fields ( only their names )
    """
    return execute_and_fetch(_TABLE_FIELDS.format(db, table))


def table_fields_data(db, table):
    """
    Return a list of table fields ( All data )
    """
    return execute_and_fetch(_TABLE_FIELDS.format(db, table))


def add_field(db, table, field_name, field_type):
    """
    Add field to table at db
    """
    if isinstance(field_type, Mysql_Type):
        field_type = Mysql_Type.eval(field_type)
    execute_only(_ADD_COLUMN.format(db, table, field_name, field_type))


def remove_field(db, table, field_name):
    """
    Remove field from table at db
    """
    execute_only(_DELETE_COLUMN.format(db, table, field_name))


def change_field(db, table, field_name, new_field, field_type):
    """
    Change field in table at db
    """
    if isinstance(field_type, Mysql_Type):
        field_type = field_type.printf
    execute_only(
        _CHANGE_COLUMN.format(
            db, table, field_name, new_field, field_type
        )
    )


def make_table(db, table, **kwargs):
    """
    Create a table at database with kwargs as fields
    """
    cp = kwargs
    for field, _type in kwargs.items():
        if isinstance(_type, Mysql_Type):
            cp[field] = Mysql_Type.eval(_type)
    execute_only(_CT_QUERY(db, table, **cp))


def remove_table(db, table):
    """
    Drop table at db
    """
    return execute_only(_DELETE_TABLE.format(db, table))


def table_content(db, table):
    """
    return a 2 dimentioanl array cont-aining all table values
    """
    #XXX: Substitute of : `select * from table`
    return execute_and_fetch(_SELECT_TABLE.format(db, table))


def table_primary_start(db, table, start):
    """
    Set table starting point for AUTO_INCREMENT PRIMARY Key
    """
    return execute_only(_AUTOINCR.format(db, table, start))


def copy_table(db, table, target_table):
    """
    Not Implemented
    """
    pass


def add_element(db, table, **kwargs):
    """
    add element to table at db
    """
    return execute_only(_IE_QUERY(db, table, **kwargs), commit=True)


def remove_elements(db, table, with_limit=-1, where=None):
    """
    Remove Element from table at db
    """
    return execute_only(
        _DL_QUERY(
            db, table, where, with_limit
        ), commit=True
    )


def select_elements(db, table, with_limit=-1, selection=None, where=None):
    """
    Select elements that satisfy kwargs from table at db
    """
    return execute_and_fetch(
        _SL_QUERY(
            db, table, where, with_limit, selection
        )
    )


def update_element(db, table, with_limit=-1, sets=None, where=None):
    """
    Update element
    """
    return execute_only(
        _UE_QUERY(
            db, table, where, with_limit, sets
        ), commit=True
    )


def select_optimised(db, table, with_limit=1, selection="*", kind="ASC",
                     sorted_by=None):
    """
    Select optimised
    """
    return execute_and_fetch(
        _SELECT_OPTI.format(
            selection, db, table, sorted_by, kind, with_limit
        )
    )
