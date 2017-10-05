

class ZileanUsers(BasicTable, WithGrantsOptions, WithLockOptions):

    db = "mysql"
    table = "user"
    fields = []

    def __init__(self):
        BasicTable.__init__(self)

    # +/- User
    @staticmethod
    def create_user(user, host, password=_DEFAULT_PASSWORD):
        """
        Add User to mysql server configuration
        """
        M.execute(ADD_USER.format(user, host, password))

    @staticmethod
    def remove_user(user, host):
        """
        Remove User from mysql server configuration
        """
        M.execute(DROP_USER.format(user, host))

    @classmethod
    def users_list(cls, filter_by=['User', 'Host']):
        """
        Return list of users filtred by filtred_by + *args
        """
        from greww.utils.str_bin import convert_bin_to_str

        s = filter_by[0]
        for _ in filter_by[1::]:
            s = "{0}, {1}".format(s, _)
        res = M.select_elements(cls.db,
                                cls.table,
                                selection=s)
        _res = []
        _t = []
        for elements in res:
            _t = ()
            for i in elements:
                _t += (convert_bin_to_str(i),)
            _res += [_t]
        return _res

    # grants

    @classmethod
    def _compare_users_to_registred_machines(cls):
        """
        """
        raise NotImplemented()
