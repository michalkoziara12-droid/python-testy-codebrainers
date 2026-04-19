import pytest
from pytest_cwiczenia.adding import adding

@pytest.mark.parametrize("num1, num2, expected", [
    (2, 3, 5),
    (3, 6, 9),
    (5, 10, 15),
    (5, -3, 2)
])
def test_adding_positive(num1, num2, expected):
    assert adding(num1, num2) == expected