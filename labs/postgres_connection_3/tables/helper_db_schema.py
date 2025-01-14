from sqlalchemy import text

PUBLIC_TABLES = ['django_migrations',
                 'django_content_type',
                 'django_admin_log',
                 'auth_permission',
                 'auth_group',
                 'auth_group_permissions',
                 'authentication_customuser',
                 'authentication_customuser_groups',
                 'authentication_customuser_user_permissions',
                 'author_author',
                 'author_author_books',
                 'book_book',
                 'order_order',
                 'django_session']


class DbSchema:
    __table_schema__ = 'public'

    def __init__(self, session):
        self.session = session

    def get_count_public_tables(self):
        query = """SELECT COUNT(table_schema)
                    FROM information_schema.tables
                    WHERE table_schema = :schema;"""
        result = self.session.execute(text(query), {'schema': self.__table_schema__}).scalar()
        return result

    def get_names_public_tables(self):
        query = """SELECT table_name 
                    FROM information_schema.tables 
                    WHERE table_schema = :schema;"""
        result = self.session.execute(text(query), {'schema': self.__table_schema__}).fetchall()
        # print(result)
        return [row[0] for row in result]

    def get_count_column_names(self, table_name):
        query = """SELECT COUNT(column_name) 
                   FROM information_schema.columns 
                   WHERE table_schema = :schema AND table_name = :table;"""
        result = self.session.execute(text(query), {'schema': self.__table_schema__, 'table': table_name}).scalar()
        return result

    def get_column_names(self, table_name):
        query = """SELECT column_name 
                       FROM information_schema.columns 
                       WHERE table_schema = :schema AND table_name = :table;"""
        result = self.session.execute(text(query),
                                      {'schema': self.__table_schema__, 'table': table_name}).fetchall()
        return [row[0] for row in result]

    def get_column_types(self, table_name):
        query = """SELECT column_name, data_type 
                   FROM information_schema.columns 
                   WHERE table_schema = :schema AND table_name = :table;"""
        result = self.session.execute(text(query), {'schema': self.__table_schema__, 'table': table_name}).fetchall()
        return {row[0]: row[1] for row in result}

    def get_nullable_columns_yes(self, table_name):
        query = """ SELECT column_name, is_nullable
                    FROM information_schema.columns
                    WHERE table_schema = :schema AND table_name = :table AND is_nullable = 'YES';"""
        result = self.session.execute(text(query), {'schema': self.__table_schema__, 'table': table_name}).fetchall()
        return {row[0]: row[1] for row in result}

    def get_nullable_columns_no(self, table_name):
        query = """ SELECT column_name, is_nullable
                    FROM information_schema.columns
                    WHERE table_schema = :schema AND table_name = :table AND is_nullable = 'NO';"""
        result = self.session.execute(text(query), {'schema': self.__table_schema__, 'table': table_name}).fetchall()
        return {row[0]: row[1] for row in result}

    def get_constraints_names(self, table_name):
        query = """SELECT constraint_name, column_name
                    FROM information_schema.key_column_usage
                    WHERE table_schema = :schema
                    AND table_name = :table;"""
        result = self.session.execute(text(query), {'schema': self.__table_schema__, 'table': table_name}).fetchall()
        return {row[0]: row[1] for row in result}

    def get_constraint_type_primary_key(self, table_name):
        query = """SELECT
                        kcu.column_name,
                        tc.constraint_type                        
                    FROM
                        information_schema.table_constraints AS tc
                    LEFT JOIN
                        information_schema.key_column_usage AS kcu
                    ON
                        tc.constraint_name = kcu.constraint_name
                        AND tc.table_schema = kcu.table_schema
                        AND tc.table_name = kcu.table_name
                    WHERE
                        tc.table_schema = :schema
                        AND tc.table_name = :table
                        AND tc.constraint_type = 'PRIMARY KEY';"""
        result = self.session.execute(text(query), {'schema': self.__table_schema__, 'table': table_name}).fetchall()
        return {row[0]: row[1] for row in result}

    def get_constraints_type_unique(self, table_name):
        query = """SELECT
                        kcu.column_name,
                        tc.constraint_type                        
                    FROM
                        information_schema.table_constraints AS tc
                    LEFT JOIN
                        information_schema.key_column_usage AS kcu
                    ON
                        tc.constraint_name = kcu.constraint_name
                        AND tc.table_schema = kcu.table_schema
                        AND tc.table_name = kcu.table_name
                    WHERE
                        tc.table_schema = :schema
                        AND tc.table_name = :table
                        AND tc.constraint_type = 'UNIQUE';"""
        result = self.session.execute(text(query), {'schema': self.__table_schema__, 'table': table_name}).fetchall()
        return {row[0]: row[1] for row in result}

    def get_constraints_type_check(self, table_name):
        query = """SELECT
                        cc.check_clause,
                        tc.constraint_type                    
                    FROM
                        information_schema.table_constraints AS tc
                    LEFT JOIN
                        information_schema.key_column_usage AS kcu
                    ON
                        tc.constraint_name = kcu.constraint_name
                        AND tc.table_schema = kcu.table_schema
                        AND tc.table_name = kcu.table_name
                    LEFT JOIN
                        information_schema.check_constraints AS cc
                    ON
                        tc.constraint_name = cc.constraint_name
                    WHERE
                        tc.table_schema = :schema
                        AND tc.table_name = :table
                        AND tc.constraint_type = 'CHECK';"""
        result = self.session.execute(text(query), {'schema': self.__table_schema__, 'table': table_name}).fetchall()

        new_result = []
        for tp in result:
            re_key = tp[0].replace(' IS NOT NULL', '')
            value = tp[1]
            re_dict = {re_key: value}
            new_result.append(re_dict)
        # return {row[0]: row[1] for row in new_result}
        return new_result


if __name__ == "__main__":
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session
    from labs.postgres_connection_3.conftest import CONNECTION_ROW

    # print(len(PUBLIC_TABLES))

    engine = create_engine(CONNECTION_ROW)
    try:
        with Session(engine) as db_session:
            schema = DbSchema(db_session)

            # print("count_public_tables:", schema.get_count_public_tables())
            # print("Names of the tables:", schema.get_names_public_tables())

            # AUTHENTICATION_CUSTOMUSER
            # print("Column count of authentication_customuser: ",
            #       schema.get_count_column_names('authentication_customuser'))
            # print("Column names of authentication_customuser: ",
            #       schema.get_column_names('authentication_customuser'))
            # print("Column types of authentication_customuser: ",
            #       schema.get_column_names('authentication_customuser'))
            # print("Nullable columns of authentication_customuser:",
            #       schema.get_nullable_columns_yes('authentication_customuser'))
            # print("Not Nullable columns of authentication_customuser:",
            #       schema.get_nullable_columns_no('authentication_customuser'))
            # print("Constraint columns of authentication_customuser:",
            #       schema.get_constraints_names('authentication_customuser'))
            # print("PK of authentication_customuser:",
            #       schema.get_constraint_type_primary_key('authentication_customuser'))
            # print("UNIQUE of authentication_customuser:",
            #       schema.get_constraints_type_unique('authentication_customuser'))

            # print("CHECK of authentication_customuser:")
            res = schema.get_constraints_type_check('authentication_customuser')
            print(type(res))

    finally:
        engine.dispose()
