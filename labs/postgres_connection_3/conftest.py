import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

# postgresql+psycopg2 - dialect[+driver], dialect is a database name, driver the name of a DBAPI
CONNECTION_ROW = "postgresql+psycopg2://postgres:postgres@localhost:5432/mentor_postgres_test"


@pytest.fixture(scope="module")
def db_engine():
    """Connection to the db"""
    engine = create_engine(CONNECTION_ROW)
    yield engine
    engine.dispose()


@pytest.fixture(scope="function")
def db_session(db_engine):
    """ Session Object for executing queries.
    SQLAlchemy automatically manages cursors across sessions,
    and the db_session fixture replaces the need to create a fixture for Cursor."""
    with Session(db_engine) as session:
        yield session
