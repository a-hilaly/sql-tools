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

User = "TESTUSER"
Host = "TESTHOST"
Password = "--"


def test_mysql_users_basics():
    #CREATE USER
    create_user(User, Host, Password)
    #LIST ALL
    ln = users_list()
    assert (User, Host, 'N') in ln
    #REMOVE USER
    remove_user(User, Host)
    ln = users_list()
    assert not (User, Host, 'N') in ln
    

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
