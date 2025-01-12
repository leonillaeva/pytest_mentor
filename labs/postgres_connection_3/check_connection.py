from sqlalchemy import create_engine
from sqlalchemy import select
from sqlalchemy.orm import sessionmaker
from sqlalchemy import asc, desc
# from db import session
# import tables
from labs.postgres_connection_3.tables.authentication_customuser import AuthCustomer

if __name__ == "__main__":
    CONNECTION_ROW = "postgresql+psycopg2://postgres:postgres@localhost:5432/mentor_postgres_test"
    engine = create_engine(CONNECTION_ROW)

    try:
        connection = engine.connect()
        print("Connection successful")
        connection.close()
    except Exception as e:
        print("Error connection:", e)

    Session = sessionmaker(
        bind=engine,
        autoflush=False,
        autocommit=False
    )
    session = Session()

    first_result = session.query(AuthCustomer.id, AuthCustomer.first_name, AuthCustomer.last_name).first()

    # all - returns list of tuples
    all_result = session.query(AuthCustomer.id, AuthCustomer.first_name, AuthCustomer.last_name).all()

    user_result = session.query(AuthCustomer.id, AuthCustomer.first_name, AuthCustomer.last_name
                                ).filter(AuthCustomer.id == 37).one_or_none()

    users_result = session.query(AuthCustomer.id, AuthCustomer.first_name, AuthCustomer.last_name
                                 ).filter(AuthCustomer.id >= 20,
                                          AuthCustomer.id <= 30).all()

    # generation of query script sql, for - id
    sub_sql_ids = session.query(AuthCustomer.id).filter(AuthCustomer.id >= 30).subquery()

    # # in, select
    sub_res_ids = session.query(AuthCustomer.first_name, AuthCustomer.last_name
                                ).filter(AuthCustomer.id.in_(select(sub_sql_ids))
                                         ).all()

    # order_by
    order_items = session.query(AuthCustomer.id, AuthCustomer.first_name, AuthCustomer.last_name
                                ).filter(AuthCustomer.id >= 20, AuthCustomer.id <= 30
                                         ).order_by(desc(AuthCustomer.id)
                                                    ).all()

    # limit
    # [(30, 'Posm', 'Second'), (29, 'Postman', 'First'), (27, '3New', 'Last'), (25, '1New', 'User'), (24, 'Visitor1', 'Form')]
    order_items_limit = session.query(AuthCustomer.id, AuthCustomer.first_name,
                                      AuthCustomer.last_name
                                      ).filter(AuthCustomer.id >= 20,
                                               AuthCustomer.id <= 30
                                               ).order_by(desc(AuthCustomer.id)
                                                          ).limit(5).all()

    # limit + offset
    # [(24, 'Visitor1', 'Form')]
    order_items_lim_offset = session.query(AuthCustomer.id, AuthCustomer.first_name,
                                           AuthCustomer.last_name
                                           ).filter(AuthCustomer.id >= 20,
                                                    AuthCustomer.id <= 30
                                                    ).order_by(desc(AuthCustomer.id)
                                                               ).limit(1).offset(4).all()

    # where ? - returns all results without filter
    # where_ids = session.query(
    #     AuthCustomer.id,
    #     AuthCustomer.first_name,
    #     AuthCustomer.last_name
    # ).filter(
    #     exists().where(AuthCustomer.id >= 30)
    # ).all()

    print("First: ", first_result)
    print("All result: ", all_result)

    if user_result:
        print("User is found: ", user_result)
    else:
        print("User is not found", user_result)

    print("Filter users: ", users_result)
    print("Subquery: ", sub_sql_ids)
    print("Ids in subquery: ", sub_res_ids)

    print("Order by: ", order_items)
    print("Limit: ", order_items_limit)
    print("Offset: ", order_items_lim_offset)
    #print(where_ids)

# .first() returns first result
# .all() returns all result
# .one_or_none() with condition (certain user, returns object's data or none)

# generation query script .subquery()
# Subquery:  SELECT authentication_customuser.id
# FROM authentication_customuser
# WHERE authentication_customuser.id >= :id_1
