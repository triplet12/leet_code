import pytest
from palindrome import palindrome


@pytest.mark.parametrize("s", [
    "A man, a plan, a canal: Panama",
    "No 'x' in Nixon",
    "racecar",
    "12321",
    "Aa",          # разный регистр
    "a",           # один символ
    "",            # пустая строка
    " ",           # только пробел
    ".,!",         # только не буквы и не цифры
])
def test_is_palindrome(s):
    assert palindrome(s) is True


@pytest.mark.parametrize("s", [
    "race a car",
    "ab",
    "0P",          # цифра и буква — классическая ловушка с LeetCode
    "hello",
])
def test_is_not_palindrome(s):
    assert palindrome(s) is False