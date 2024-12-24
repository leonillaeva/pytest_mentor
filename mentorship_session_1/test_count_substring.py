import pytest
from unittest.mock import patch
from mentorship_session_1.helper import count_substring, outcome

# using constant with iter to use in pytest.mark.parametrize
TEST_COUNT_SUBSTRING = [
        # pytest.param with marks like: pytest.mark.xfail, pytest.mark.skip are pytest module features for automation
        pytest.param('banana', 'na', 2, marks=[pytest.mark.xfail]),
        pytest.param('banana', 'na', 3, marks=[pytest.mark.xfail]),
                    ('apple', 'p', 3),
                    ('hello world', 'o', 2),
                    ('aaaaaa', 'aa', 3),
                    ('test', 'x', 0),
                    ('this is a list, this is a tuple, this is a string', 'this', 3)
    ]

@pytest.mark.parametrize('txt, sub_txt, expected_count', TEST_COUNT_SUBSTRING)
def test_count_substring(txt, sub_txt, expected_count):
    result = count_substring(txt, sub_txt)
    assert result == expected_count

def test_outcome(mock_input_prompts, capsys):
    print('\nBefore Patching\n')
    with patch('builtins.input', new=mock_input_prompts):
        outcome()
    print('\nAfter Patching\n')

    # capture output
    captured = capsys.readouterr()
    #assert 'the substring "na" appears 2 times in "banana"' in captured.out # partial
    assert captured.out == 'the substring "na" appears 2 times in "banana"\n'

# Example of test for checking if valid Exception is thrown
def test_raises():
    try:
       # Generating IndexError exception
       array = [1,2,3]
       array[10]
       # Generating ZeroDivisionError exception
       # 0/0
    # Checking online ZeroDivisionError, if yes - pass test
    except ZeroDivisionError:
        assert True
    except Exception:
        # If any other Exception - test fail
        assert False, "Test failed with not expected exception"
        # Text after assert equalation is good for verification of test fails
