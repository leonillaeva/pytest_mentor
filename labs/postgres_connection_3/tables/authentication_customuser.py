# импортируем поля
from sqlalchemy import Boolean, Column, Integer, String, DateTime, text
from db import Model


class AuthCustomer(Model):
    __tablename__ = 'authentication_customuser'

    id = Column(Integer, primary_key=True)  # это ключ
    first_name = Column(String)
    last_name = Column(String)
    middle_name = Column(String)
    password_hash = Column(String)
    email = Column(String, index=True)
    role = Column(Integer)

    last_login = Column(DateTime(timezone=True))
    created_at = Column(DateTime(timezone=True))
    updated_at = Column(DateTime(timezone=True))

    is_active = Column(Boolean)
    is_superuser = Column(Boolean)
    is_staff = Column(Boolean)



