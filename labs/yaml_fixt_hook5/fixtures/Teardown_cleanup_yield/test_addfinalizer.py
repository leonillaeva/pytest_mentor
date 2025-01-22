# from emaillib_classes import Email, MailAdminClient
import pytest
#
#
# @pytest.fixture
# def mail_admin():
#     return MailAdminClient()
#
#
# @pytest.fixture
# def sending_user(mail_admin):
#     user = mail_admin.create_user()
#     yield user
#     mail_admin.delete_user(user)
#
#
# @pytest.fixture
# def receiving_user(mail_admin, request):
#     user = mail_admin.create_user()
#
#     def delete_user():
#         mail_admin.delete_user(user)
#
#     request.addfinalizer(delete_user)
#     return user
#
#
# @pytest.fixture
# def email(sending_user, receiving_user, request):
#     _email = Email(subject="Hey!", body="How's it going?")
#     sending_user.send_email(_email, receiving_user)
#
#     def empty_mailbox():
#         receiving_user.clear_mailbox()
#
#     request.addfinalizer(empty_mailbox)
#     return _email
#
#
# def test_email_received(receiving_user, email):
#     assert email in receiving_user.inbo

# -----------------------------
import pytest


# def test_bar(fix_w_yield1, fix_w_yield2):
#     print("test_bar")
#
#
# @pytest.fixture
# def fix_w_yield1():
#     yield
#     print("after_yield_1")
#
#
# @pytest.fixture
# def fix_w_yield2():
#     yield
#     print("after_yield_2")

# -----------------
from functools import partial
import pytest


@pytest.fixture
def fix_w_finalizers(request):
    request.addfinalizer(partial(print, "finalizer_2"))
    request.addfinalizer(partial(print, "finalizer_1"))


def test_bar(fix_w_finalizers):
    print("test_bar")