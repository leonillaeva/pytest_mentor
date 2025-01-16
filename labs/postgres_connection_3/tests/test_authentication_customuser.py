from labs.postgres_connection_3.tables.authentication_customuser import AuthCustomer


def test_get_user_by_id(db_session):
    user = db_session.query(AuthCustomer.id, AuthCustomer.first_name, AuthCustomer.last_name).filter(
        AuthCustomer.id == 20
    ).one_or_none()
    # print(user.id, user.first_name, user.last_name)
    expected = (20, "New", "Lib")
    assert user == expected
#
# def test_number_of_columns(db_session):
#     result = db_session.execute("""
#         SELECT COUNT(column_name) AS number_columns
#         FROM information_schema.columns
#         WHERE table_schema = 'public' AND table_name = 'authentication_customuser';
#     """)
#     count = result.scalar()
#     assert count == 12, f"Expected 12 columns, but got {count}"
