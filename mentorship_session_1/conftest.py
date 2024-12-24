import pytest

# Use conftest.py for in pytest module as "storage" for fixtures
@pytest.fixture
def mock_input_prompts():
    prompts = iter(['Enter a string >', 'Enter a substring >'])
    values = iter(['banana', 'na'])

    def mock_input(prompt):
        assert prompt == next(prompts)
        return next(values)

    # return mock_input
    yield mock_input
    # Difference between return and yield:
    # - return mock_input will finish using mock_input_prompts() function
    # - yield mock_input will return to mock_input_prompts() function and will continue wil code.
    # In this example print('hello world') will be printed after 'yield', but not after 'return'
    print('hello world')
