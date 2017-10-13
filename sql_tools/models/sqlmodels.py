from .sql_io import SQLio
from sql_tools.utils import refetch_filter
from .keymap import (
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
    _CREATE_TABLE_LIKE,
    _INSERT_TABLE_CONTENT,
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
    ADD_USER,
    DROP_USER,
    LOCK_USER,
    UNLOCK_USER,
    GRANT_POWER,
    REVOKE_POWER,
    USER_GRANTS
)

class SimpleSQLModel(SQLio):

    def __init__(self, system):
        SQLio.__init__(self, system)

    @property
    def system(self):
        """
        Return system type
        """
        return self.CNX._system

    @refetch_filter([0])
    @property
    def version(self):
        """
        Return system version
        """
        return self.execute_and_fetch(_VERSION)

    @refetch_filter([0])
    @property
    def user(self):
        """
        Return session user
        """
        return self.execute_and_fetch(_USER)

    @refetch_filter([0])
    def databases(self):
        """
        Return list of all databases
        """
        return self.execute_and_fetch(_SHOW_DATABASES)

    def make_database(self, db):
        """
        Create database
        """
        self.execute_only(_CREATE_DATABASE.format(db))

    def remove_database(self, db):
        """
        Drop database
        """
        self.execute_only(_DELETE_DATABASE.format(db))

    @refetch_filter([0])
    def tables(self, db):
        """
        """
        return self.execute_and_fetch(_SHOW_TABLES.format(db))

    @refetch_filter([0])
    def table_fields(self, db, table):
        """
        Return a list of table fields ( only their names )
        """
        return self.execute_and_fetch(_TABLE_FIELDS.format(db, table))

    def table_fields_data(self, db, table):
        """
        Return a list of table fields ( All data )
        """
        return self.execute_and_fetch(_TABLE_FIELDS.format(db, table))

    def add_field(self, db, table, field_name, field_type):
        """
        Add field to table at db
        """
        if isinstance(field_type, SQLType):
            field_type = SQLType.eval(field_type)
        self.execute_only(
            _ADD_COLUMN.format(db, table, field_name, field_type)
        )

    def remove_field(self, db, table, field_name):
        """
        Remove field from table at db
        """
        self.execute_only(_DELETE_COLUMN.format(db, table, field_name))


    def change_field(self, db, table, field_name, new_field, field_type):
        """
        Change field in table at db
        """
        if isinstance(field_type, SQLType):
            field_type = field_type.printf
        self.execute_only(
            _CHANGE_COLUMN.format(
                db, table, field_name, new_field, field_type
            )
        )


    def make_table(self, db, table, from_another_table=None, **kwargs):
        """
        Create a table at database with kwargs as fields
        """
        if from_another_table:
            self.execute_only(_CREATE_TABLE_LIKE.format(db, table, from_another_table))
            return
        cp = kwargs
        for field, _type in kwargs.items():
            if isinstance(_type, SQLType):
                cp[field] = SQLType.eval(_type)
        self.execute_only(_CT_QUERY(db, table, **cp))


    def remove_table(self, db, table):
        """
        Drop table at db
        """
        return self.execute_only(_DELETE_TABLE.format(db, table))


    def table_content(self, db, table):
        """
        return a 2 dimentioanl array containing all table values
        """
        #XXX: Substitute of : `select * from table`
        return self.execute_and_fetch(_SELECT_TABLE.format(db, table))


    def table_primary_start(self, db, table, start):
        """
        Set table starting point for AUTO_INCREMENT PRIMARY Key
        """
        return self.execute_only(_AUTOINCR.format(db, table, start))


    def pour_table_in(self, db, table, totable):
        """
        Pour table content into another table
        Tables should have same fields names and types
        """
        self.execute_only(
            _INSERT_TABLE_CONTENT.format(
                db, totable, table
            ), commit=True
        )


    def copy_table(self, db, table, target_table, exists=False):
        """
        Create a copy of another table
        """
        if not exists:
            self.make_table(db, table, from_another_table=target_table)
        self.pour_table_in(db, target_table, table)


    def add_element(self, db, table, **kwargs):
        """
        add element to table at db
        """
        return self.execute_only(_IE_QUERY(db, table, **kwargs), commit=True)


    def remove_elements(self, db, table, with_limit=-1, where=None):
        """
        Remove Element from table at db
        """
        return self.execute_only(
            _DL_QUERY(
                db, table, where, with_limit
            ), commit=True
        )


    def select_elements(self, db, table, with_limit=-1, selection=None,
                        where=None):
        """
        Select elements that satisfy kwargs from table at db
        """
        return self.execute_and_fetch(
            _SL_QUERY(
                db, table, where, with_limit, selection
            )
        )


    def update_element(self, db, table, with_limit=-1, sets=None, where=None):
        """
        Update element
        """
        return self.execute_only(
            _UE_QUERY(
                db, table, where, with_limit, sets
            ), commit=True
        )


    def select_optimised(self, db, table, with_limit=1, selection="*", kind="ASC",
                         sorted_by=None):
        """
        Select optimised
        """
        return self.execute_and_fetch(
            _SELECT_OPTI.format(
                selection, db, table, sorted_by, kind, with_limit
            )
        )


class AdminSQLModel(SimpleSQLModel):

    def __init__(self, system):
        SimpleSQLModel.__init__(self, system)

    def create_user(self, user, host, password):
        """
        Add User to mysql server configuration
        """
        self.execute_only(ADD_USER.format(user, host, password))


    def remove_user(self, user, host):
        """
        Remove User from mysql server configuration
        """
        self.execute_only(DROP_USER.format(user, host))


    def users_list(self, filter_by=['User', 'Host', 'account_locked']):
        """
        Return list of users filtred by filtred_by + *args
        """
        s = listify(filter_by)
        res = self.select_elements('mysql', 'user', selection=s)
        if isinstance(res[0][0], str):
            return res
        _res = []
        _t = []
        for elements in res:
            _t = ()
            for i in elements:
                if isinstance(i, str):
                    _t += (i, )
                    continue
                _t += (bin2str(i), )
            _res += [_t]
        return _res

    def lock_user(self, user, host):
        """
        Show User grants
        """
        self.execute_only(LOCK_USER.format(user, host))


    def unlock_user(self, user, host):
        """
        Show User grants
        """
        self.execute_only(UNLOCK_USER.format(user, host))


    def set_user_grants(self, user, host, grants=None, database=None,
                        table=None):
        """
        Grants rights to user
        """
        g, d, t = kwgs(grants, database, table)
        self.execute_only(GRANT_POWER.format(g, d, t, user, host))


    def revoke_user_grants(self, user, host, grants=None, database=None,
                           table=None):
        """
        Revoke rights
        """
        g, d, t = kwgs(grants, database, table)
        self.execute_only(REVOKE_POWER.format(g, d, t, user, host))


    @refetch_filter([0])
    def user_grants(self, user, host):
        """
        Show User grants
        """
        return self.execute_and_fetch(USER_GRANTS.format(user, host))
