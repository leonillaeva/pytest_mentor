from labs.postgres_connection_3.tables.helper_db_schema import DbSchema, PUBLIC_TABLES

AUTHENTICATION_CUSTOMUSER_COLUMNS = ['last_login', 'first_name', 'last_name', 'middle_name', 'email', 'password',
                                     'created_at', 'updated_at', 'role', 'is_active', 'id', 'is_staff', 'is_superuser']

PK = 'PRIMARY KEY'
UNIQUE = 'UNIQUE'
CHECK = 'CHECK'

integer = 'integer'
character_varying = 'character varying'
timestamp_zone = 'timestamp with time zone'
boolean = 'boolean'

null_yes = 'YES'
null_no = 'NO'


class TestDbSchema:

    def test_get_count_public_tables(self, db_session):
        schema = DbSchema(db_session)
        count = schema.get_count_public_tables()
        # print(count)
        assert count == 14, "ERROR! Expected 14 tables"

    def test_get_names_public_tables(self, db_session):
        schema = DbSchema(db_session)
        tables = schema.get_names_public_tables()
        assert len(tables) == 14, "14 tables"
        assert set(PUBLIC_TABLES).issubset(set(tables)), "ERROR! All names of the PUBLIC_TABLES should be in the tables"


# AUTHENTICATION_CUSTOMUSER
class TestAuthenticationCustomuserSchema:

    def test_get_count_column_names_authentication_customuser(self, db_session):
        schema = DbSchema(db_session)
        count = schema.get_count_column_names('authentication_customuser')
        assert count == 13, "ERROR! Expected 13 number of columns in 'authentication_customuser'"

    def test_get_column_names_authentication_customuser(self, db_session):
        schema = DbSchema(db_session)
        columns = schema.get_column_names('authentication_customuser')
        assert len(columns) == 13
        assert set(columns) == set(AUTHENTICATION_CUSTOMUSER_COLUMNS), "ERROR! Columns are not matched"

    def test_get_column_types_authentication_customuser(self, db_session):
        schema = DbSchema(db_session)
        column_types = schema.get_column_types('authentication_customuser')
        assert column_types['last_login'] == timestamp_zone
        assert column_types['first_name'] == character_varying
        assert column_types['last_name'] == character_varying
        assert column_types['middle_name'] == character_varying
        assert column_types['email'] == character_varying, "ERROR! Expected column type 'email' is 'character_varying'"
        assert column_types['password'] == character_varying, "ERROR! Exp column type 'password' is 'character_varying'"
        assert column_types['created_at'] == timestamp_zone
        assert column_types['updated_at'] == timestamp_zone
        assert column_types['role'] == integer
        assert column_types['is_active'] == boolean
        assert column_types['id'] == integer, "ERROR! Expected column type 'id' is 'integer"
        assert column_types['is_staff'] == boolean
        assert column_types['is_superuser'] == boolean

    def test_get_nullable_columns_yes_authentication_customuser(self, db_session):
        schema = DbSchema(db_session)
        nullable_columns = schema.get_nullable_columns_yes('authentication_customuser')
        assert len(nullable_columns) == 1
        assert nullable_columns['last_login'] == null_yes, "ERROR! Expected null column is 'last_login"

    def test_get_nullable_columns_no_authentication_customuser(self, db_session):
        schema = DbSchema(db_session)
        not_nullable_columns = schema.get_nullable_columns_no('authentication_customuser')
        assert len(not_nullable_columns) == 12
        assert not_nullable_columns['first_name'] == null_no, "ERROR! Expected NO null column is 'first_name"
        assert not_nullable_columns['last_name'] == null_no
        assert not_nullable_columns['middle_name'] == null_no
        assert not_nullable_columns['email'] == null_no
        assert not_nullable_columns['password'] == null_no
        assert not_nullable_columns['created_at'] == null_no
        assert not_nullable_columns['updated_at'] == null_no
        assert not_nullable_columns['role'] == null_no
        assert not_nullable_columns['is_active'] == null_no
        assert not_nullable_columns['id'] == null_no
        assert not_nullable_columns['is_staff'] == null_no
        assert not_nullable_columns['is_superuser'] == null_no

    def test_get_constraint_names(self, db_session):
        schema = DbSchema(db_session)
        constraints = schema.get_constraints_names('authentication_customuser')
        assert len(constraints) == 2
        assert constraints['authentication_customuser_pkey'] == 'id'
        assert constraints['authentication_customuser_email_key'] == 'email'

    def test_get_constraint_type_primary_key(self, db_session):
        schema = DbSchema(db_session)
        pk_constraint = schema.get_constraint_type_primary_key('authentication_customuser')
        assert len(pk_constraint) == 1
        assert pk_constraint['id'] == PK, 'ERROR! PK is id'

    def test_get_constraints_type_unique(self, db_session):
        schema = DbSchema(db_session)
        unique_constraints = schema.get_constraints_type_unique('authentication_customuser')
        assert len(unique_constraints) == 1
        assert unique_constraints['email'] == UNIQUE, 'ERROR! UNIQUE is email'

    def test_get_constraints_type_check(self, db_session):
        list_check = [{'first_name': 'CHECK'}, {'last_name': 'CHECK'}, {'middle_name': 'CHECK'}, {'email': 'CHECK'},
                      {'password': 'CHECK'}, {'created_at': 'CHECK'}, {'updated_at': 'CHECK'}, {'role': 'CHECK'},
                      {'is_active': 'CHECK'}, {'id': 'CHECK'}, {'is_staff': 'CHECK'}, {'is_superuser': 'CHECK'}]

        schema = DbSchema(db_session)
        check_constraints = schema.get_constraints_type_check('authentication_customuser')
        assert len(check_constraints) == 12
        assert check_constraints == list_check, "ERROR! CHECK items are not matched"
        # assert check_constraints[0]['first_name'] == CHECK, 'ERROR! CHECK is first_name'
        # assert check_constraints[1]['last_name'] == CHECK, 'ERROR! CHECK is last_name'
        # assert check_constraints[2]['middle_name'] == CHECK
        # assert check_constraints[2]['middle_name'] == CHECK


# AUTHOR
class TestAuthorSchema:
    def test_get_count_column_names_author_author(self, db_session):
        pass

    def test_get_column_names_author_author(self, db_session):
        pass

    def test_get_column_types_author_author(self, db_session):
        pass
