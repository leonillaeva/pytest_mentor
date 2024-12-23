import pytest
from unittest.mock import patch
from count_argument_reference import get_string_and_substring, count_substring, outcome


@pytest.fixture
def mock_input_prompts():
    prompts = iter(['Enter a string >', 'Enter a substring >'])
    values = iter(['banana', 'na'])

    def mock_input(prompt):
        assert prompt == next(prompts)
        return next(values)

    return mock_input


def test_get_string_and_substring(mock_input_prompts):
    with patch('builtins.input', new=mock_input_prompts):
        result = get_string_and_substring()
        assert result == ('banana', 'na')


@pytest.mark.parametrize(
    'txt, sub_txt, expected_count',
    [
        ('banana', 'na', 2),
        ('apple', 'p', 2),
        ('hello world', 'o', 2),
        ('aaaaaa', 'aa', 3),
        ('test', 'x', 0),
        ('this is a list, this is a tuple, this is a string', 'this', 3)
    ]
)
def test_count_substring(txt, sub_txt, expected_count):
    result = count_substring(txt, sub_txt)
    assert result == expected_count


def test_outcome(mock_input_prompts, capsys):
    with patch('builtins.input', new=mock_input_prompts):
        outcome()

    # capture output
    captured = capsys.readouterr()
    #assert 'the substring "na" appears 2 times in "banana"' in captured.out # partial
    assert captured.out == 'the substring "na" appears 2 times in "banana"\n'

# @pytest.fixture
# def mock_input_prompts(request):
#     # Expected prompts
#     prompts = iter(['Enter a string >', 'Enter a substring >'])
#
#     # Input values
#     values = iter(request.param)
#
#     def mock_input(prompt):
#         # Check prompts
#         assert prompt == next(prompts)
#         # return values
#         return next(values)
