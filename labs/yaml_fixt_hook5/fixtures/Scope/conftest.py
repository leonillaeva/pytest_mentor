# The smtplib module defines an SMTP client session object that can be used to send mail to any internet machine
import smtplib

import pytest


@pytest.fixture(scope="module")
def smtp_connection():
    return smtplib.SMTP("smtp.gmail.com", 587, timeout=5)


@pytest.fixture(scope="session")
def smtp_connection_session():
    # the returned fixture value will be shared for
    # all tests requesting it
    ...
