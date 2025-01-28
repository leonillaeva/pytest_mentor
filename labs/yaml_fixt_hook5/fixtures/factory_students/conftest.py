import pytest
from student import Student
from datetime import datetime


@pytest.fixture
def dummy_student():
    # print("making dummy student")
    return Student("hikhil", datetime(2000, 1, 1), "coe", 20)


# factory, generating function
@pytest.fixture
def make_dummy_student_factory():
    def _make_dummy_student(name, credits):
        return Student(name, datetime(2000, 1, 1), "coe", credits)

    return _make_dummy_student
