import pytest
import psycopg2
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# from labs.postgres_connection_3.db import Session

# postgresql+psycopg2 - dialect[+driver], dialect is a database name, driver the name of a DBAPI
CONNECTION_ROW = "postgresql://postgres:postgres@localhost:5432/mentor_postgres_test"


@pytest.fixture(scope="module")
def db_connection():
    conn = psycopg2.connect(
        dbname="mentor_postgres_test",
        user="postgres",
        password="postgres",
        host="localhost",
        port="5432"
    )
    yield conn
    conn.close()


@pytest.fixture(scope="function")
def setup_database(db_connection):
    # Create table before testing
    cursor = db_connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS test_table (
            id SERIAL PRIMARY KEY,
            name TEXT NOT NULL
        );
    """)
    db_connection.commit()
    yield cursor  # Return cursor for using in tests

    # Clear table after a test
    cursor.execute("TRUNCATE TABLE test_table;")
    db_connection.commit()
    cursor.close()


@pytest.fixture(scope="module")
def db_engine():
    engine = create_engine(CONNECTION_ROW)
    yield engine


@pytest.fixture
def db_session(db_engine):
    Session = sessionmaker(
        bind=db_engine,
        autoflush=False,
        autocommit=False
    )
    session = Session()
    try:
        yield session
        session.rollback()  # clear changing after test
    finally:
        session.close()
