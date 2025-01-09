from labs.postgres_connection_3.tables import authentication_customuser


def test_get_data_user_by_id(db_session):
    # user = db_session.query(authentication_customuser.AuthCustomer).first()
    user = db_session.query(authentication_customuser.AuthCustomer.id,
                            authentication_customuser.AuthCustomer.first_name,
                            authentication_customuser.AuthCustomer.last_name
                            ).filter(authentication_customuser.AuthCustomer.id == 20).one_or_none()
    # print(user.id, user.first_name, user.last_name)
    expected = (20, "New", "Lib")
    assert user == expected
