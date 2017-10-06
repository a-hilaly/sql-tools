from mysql_utils.logging import (
    set_user_grants,
    revoke_user_grants,
    user_grants,
    create_user,
    remove_user,
    users_list,
    lock_user,
    unlock_user,
)


def test_mysql_users_basics():
    #CREATE USER
    #REMOVE USER
    #LIST ALL
    pass


def test_mysql_users_locks():
    pass


def test_mysql_users_grants():
    #GRANTS USER
    #REVOKE GRANTS
    #SHOW GRANTS
    #GRANTS
    pass


__all__ = [test_mysql_users_basics,
           test_mysql_users_locks,
           test_mysql_users_grants]
