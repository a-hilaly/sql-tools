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
Host = "testhost"
Password = "--"


def test_mysql_users_basics():
    # init
    # CREATE USER
    create_user(User, Host, Password)
    # LIST ALL
    ln = users_list()
    assert (User, Host, 'N') in ln
    # REMOVE USER
    remove_user(User, Host)
    # Check
    ln = users_list()
    assert not (User, Host, 'N') in ln
    return 1


def test_mysql_users_locks():
    # init
    create_user(User, Host, Password)
    # LOCK USER
    lock_user(User, Host)
    # LIST ALL
    ln = users_list()
    assert (User, Host, 'Y') in ln
    # Unlock User
    unlock_user(User, Host)
    ln = users_list()
    assert (User, Host, 'N') in ln
    # Cleanup
    remove_user(User, Host)
    return 1


def test_mysql_users_grants():
    # init
    create_user(User, Host, Password)
    # SHOW GRANTS
    grants = user_grants(User, Host)
    assert grants == "GRANT USAGE ON *.* TO '{0}'@'{1}'".format(User, Host)
    # SET GRANTS
    set_user_grants(User, Host, grants="SELECT")
    grants = user_grants(User, Host)
    assert grants == "GRANT SELECT ON *.* TO '{0}'@'{1}'".format(User, Host)
    # REVOKE GRANTS
    revoke_user_grants(User, Host, 'SELECT')
    # SHOW GRANTS
    grants = user_grants(User, Host)
    assert grants == "GRANT USAGE ON *.* TO '{0}'@'{1}'".format(User, Host)
    # Cleanup
    remove_user(User, Host)
    return 1


__all__ = [test_mysql_users_basics,
           test_mysql_users_locks,
           test_mysql_users_grants]
