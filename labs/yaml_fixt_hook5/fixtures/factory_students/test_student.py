from datetime import datetime
import pytest
from student import Student, get_topper


def test_student_get_age(dummy_student):
    dummy_student_age = (datetime.now() - dummy_student.dob).days // 365
    assert dummy_student.get_age() == dummy_student_age


# def test_student_add_credits(dummy_student):
#     dummy_student.add_credits(5)
#     assert dummy_student.get_credits() == 5

def test_student_get_credits(dummy_student):
    assert dummy_student.get_credits() == 20


def test_get_topper(make_dummy_student_factory):
    students = [
        make_dummy_student_factory("john", 21),
        make_dummy_student_factory("dou", 19),
        make_dummy_student_factory("li", 22)
    ]

    topper = get_topper(students)
    assert topper == students[2]
