import pytest


@pytest.fixture
def make_customer_record():
    def _make_customer_record(name):
        return {"name": name, "orders": []}

    return _make_customer_record


def test_customer_records(make_customer_record):
    """
    :param make_customer_record:
    :return: {'name': 'Lisa', 'orders': []} {'name': 'Mike', 'orders': []} {'name': 'Meredith', 'orders': []}
    """
    customer_1 = make_customer_record("Lisa")
    customer_2 = make_customer_record("Mike")
    customer_3 = make_customer_record("Meredith")
    # print(customer_1, customer_2, customer_3)