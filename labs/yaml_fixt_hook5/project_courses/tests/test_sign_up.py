import pytest
from pages.main_page import MainPage
from pages.sign_up_page import SignUpPage


@pytest.mark.skip(reason="Validation of empty fields is not implemented")
def test_sign_up_empty_fields(driver):
    main_page = MainPage(driver)
    main_page.go_to_sign_up_page()
    sign_up_page = SignUpPage(driver)
    sign_up_page.click_element(sign_up_page.SIGN_UP_BUTTON)
    assert "This field is required" in driver.page_source


def test_sign_up_student_valid_data(driver):
    main_page = MainPage(driver)
    main_page.go_to_sign_up_page()
    sign_up_page = SignUpPage(driver)
    sign_up_page.fill_form(
        firstname="John",
        lastname="Doe",
        password="Password123!",
        confirm_password="Password123!",
        age="18",
        role="student"
    )
    sign_up_page.click_element(sign_up_page.SIGN_UP_BUTTON)
    assert "Confirmation email sent" in driver.page_source


def test_sign_up_teacher_valid_data(driver):
    main_page = MainPage(driver)
    main_page.go_to_sign_up_page()
    sign_up_page = SignUpPage(driver)
    sign_up_page.fill_form(
        firstname="John",
        lastname="Doe",
        password="Password12345",
        confirm_password="Password12345",
        age="100",
        role="teacher",
        code="12345"
    )
    sign_up_page.click_element(sign_up_page.SIGN_UP_BUTTON)
    assert "Confirmation email sent" in driver.page_source


def test_sign_up_student_not_valid_firstname(driver):
    pass


def test_sign_up_student_not_valid_lastname(driver):
    pass


def test_sign_up_student_not_valid_password(driver):
    pass


@pytest.mark.skip(reason="Validation of confirm password field is not implemented")
def test_sign_up_student_not_valid_confirm_password(driver):
    pass


@pytest.mark.xfail(reason="Error of age field is not implemented")
def test_sign_up_student_age_over(driver):
    pass


@pytest.mark.xfail(reason="Error of age field is not implemented")
def test_sign_up_student_age_less(driver):
    pass


@pytest.mark.xfail(reason="Error of age field is not implemented")
def test_sign_up_teacher_age_over(driver):
    pass


@pytest.mark.xfail(reason="Error of age field is not implemented")
def test_sign_up_teacher_age_less(driver):
    pass


@pytest.mark.xfail(reason="Verification code is not implemented")
def test_sign_up_teacher_without_code(driver):
    main_page = MainPage(driver)
    main_page.go_to_sign_up_page()
    sign_up_page = SignUpPage(driver)
    sign_up_page.fill_form(
        firstname="Jane",
        lastname="Smith",
        password="Password123!",
        confirm_password="Password123!",
        age="25",
        role="teacher"
    )
    sign_up_page.click_element(sign_up_page.SIGN_UP_BUTTON)
    assert "Verification code is required" in driver.page_source
