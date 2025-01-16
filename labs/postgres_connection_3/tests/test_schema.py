import pytest
from labs.postgres_connection_3.tables.helper_db_schema import DbSchema, PUBLIC_TABLES

AUTHENTICATION_CUSTOMUSER_COLUMNS = ['last_login', 'first_name', 'last_name', 'middle_name', 'email', 'password',
                                     'created_at', 'updated_at', 'role', 'is_active', 'id', 'is_staff', 'is_superuser']

AUTHOR_AUTHOR_COLUMNS = ['name', 'surname', 'patronymic', 'id']

PK = 'PRIMARY KEY'
UNIQUE = 'UNIQUE'
CHECK = 'CHECK'

integer = 'integer'
character_varying = 'character varying'
timestamp_zone = 'timestamp with time zone'
boolean = 'boolean'

null_yes = 'YES'
null_no = 'NO'

auth_customuser_tb_name = 'authentication_customuser'
author_tb_name = "author_author"


class TestDbSchema:

    def test_get_count_public_tables(self, db_session):
        schema = DbSchema(db_session)
        count = schema.get_count_public_tables()
        # print(count)
        assert count == 14, "ERROR! Expected 14 tables"

    @pytest.mark.smoke
    def test_get_names_public_tables(self, db_session):
        schema = DbSchema(db_session)
        tables = schema.get_names_public_tables()
        assert len(tables) == 14, "14 tables"
        assert set(PUBLIC_TABLES).issubset(set(tables)), "ERROR! All names of the PUBLIC_TABLES should be in the tables"

    @pytest.mark.xfail(reason="names of the tables are not in plural")
    def test_check_names_public_tables_plural(self, db_session):
        plural_names = ['authentication_customusers', 'authors_authors', 'authors_authors_books',
                        'books_books', 'orders_orders']
        schema = DbSchema(db_session)
        tables_names = schema.check_names_public_tables_plural()
        assert len(tables_names) == 14, "14 tables"
        assert plural_names[0] in tables_names, "ERROR! Name of table should be in plural"
        assert plural_names[1] in tables_names
        assert plural_names[2] in tables_names
        assert plural_names[3] in tables_names
        assert plural_names[4] in tables_names


# AUTHENTICATION_CUSTOMUSERS
class TestAuthenticationCustomuserSchema:

    def test_get_count_column_names(self, db_session):
        schema = DbSchema(db_session)
        count = schema.get_count_column_names(auth_customuser_tb_name)
        assert count == 13, "ERROR! Expected 13 number of columns in 'authentication_customuser'"

    @pytest.mark.smoke
    def test_get_column_names(self, db_session):
        schema = DbSchema(db_session)
        columns = schema.get_column_names(auth_customuser_tb_name)
        assert len(columns) == 13
        assert set(columns) == set(AUTHENTICATION_CUSTOMUSER_COLUMNS), "ERROR! Columns are not matched"

    def test_get_column_types(self, db_session):
        schema = DbSchema(db_session)
        column_types = schema.get_column_types(auth_customuser_tb_name)
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

    def test_get_nullable_columns_yes(self, db_session):
        schema = DbSchema(db_session)
        nullable_columns = schema.get_nullable_columns_yes(auth_customuser_tb_name)
        assert len(nullable_columns) == 1
        assert nullable_columns['last_login'] == null_yes, "ERROR! Expected null column is 'last_login"

    @pytest.mark.smoke
    def test_get_nullable_columns_no(self, db_session):
        no_columns = ['first_name', 'last_name', 'middle_name', 'email', 'password',
                      'created_at', 'updated_at', 'role', 'is_active', 'id', 'is_staff', 'is_superuser']
        schema = DbSchema(db_session)
        no_nullable_columns = schema.get_nullable_columns_no(auth_customuser_tb_name)
        assert len(no_nullable_columns) == 12

        for column in no_columns:
            assert column in no_nullable_columns, f"ERROR! '{column}' column should not be nullable"

    def test_get_constraint_names(self, db_session):
        schema = DbSchema(db_session)
        constraints = schema.get_constraints_names(auth_customuser_tb_name)
        assert len(constraints) == 2
        assert constraints['authentication_customuser_pkey'] == 'id'
        assert constraints['authentication_customuser_email_key'] == 'email'

    @pytest.mark.smoke
    def test_get_constraint_type_primary_key(self, db_session):
        schema = DbSchema(db_session)
        pk_constraint = schema.get_constraint_type_primary_key(auth_customuser_tb_name)
        assert len(pk_constraint) == 1
        assert pk_constraint['id'] == PK, 'ERROR! PK is id'

    def test_get_constraints_type_unique(self, db_session):
        schema = DbSchema(db_session)
        unique_constraints = schema.get_constraints_type_unique(auth_customuser_tb_name)
        assert len(unique_constraints) == 1
        assert unique_constraints['email'] == UNIQUE, 'ERROR! UNIQUE is email'

    def test_get_constraints_type_check(self, db_session):
        list_check = [{'first_name': 'CHECK'}, {'last_name': 'CHECK'}, {'middle_name': 'CHECK'}, {'email': 'CHECK'},
                      {'password': 'CHECK'}, {'created_at': 'CHECK'}, {'updated_at': 'CHECK'}, {'role': 'CHECK'},
                      {'is_active': 'CHECK'}, {'id': 'CHECK'}, {'is_staff': 'CHECK'}, {'is_superuser': 'CHECK'}]

        schema = DbSchema(db_session)
        check_constraints = schema.get_constraints_type_check(auth_customuser_tb_name)
        assert len(check_constraints) == 12
        assert check_constraints == list_check, "ERROR! CHECK items are not matched"


# AUTHORS
class TestAuthorSchema:

    def test_get_count_column_names(self, db_session):
        schema = DbSchema(db_session)
        count = schema.get_count_column_names(author_tb_name)
        assert count == 4, "ERROR! Expected 4 number of columns in 'author_author'"

    @pytest.mark.smoke
    def test_get_column_names(self, db_session):
        schema = DbSchema(db_session)
        columns = schema.get_column_names(author_tb_name)
        assert len(columns) == 4
        assert set(columns) == set(AUTHOR_AUTHOR_COLUMNS), "ERROR! Columns are not matched"

    def test_get_column_types(self, db_session):
        schema = DbSchema(db_session)
        column_types = schema.get_column_types(author_tb_name)
        assert column_types['name'] == character_varying
        assert column_types['surname'] == character_varying
        assert column_types['patronymic'] == character_varying
        assert column_types['id'] == integer

    def test_get_nullable_columns_yes(self, db_session):
        schema = DbSchema(db_session)
        yes_nullable_columns = schema.get_nullable_columns_yes(author_tb_name)
        assert len(yes_nullable_columns) == 0, "ERROR! There should not be YES nullable columns"

        yes_column_names = [tp[0] for tp in yes_nullable_columns]
        for column in AUTHOR_AUTHOR_COLUMNS:
            assert column not in yes_column_names, f"ERROR! '{column}' is YES nullable column"

    @pytest.mark.smoke
    def test_get_nullable_columns_no(self, db_session):
        schema = DbSchema(db_session)
        no_nullable_columns = schema.get_nullable_columns_no(author_tb_name)
        print(no_nullable_columns)
        assert len(no_nullable_columns) == 4, "ERROR! There should be 4 NO nullable columns"

        for column in AUTHOR_AUTHOR_COLUMNS:
            assert column in no_nullable_columns, f"ERROR! '{column}' is NO nullable column"

