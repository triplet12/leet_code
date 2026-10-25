import pytest
from two_sum import two_sum

@pytest.fixture
def sorted_nums() -> list[int]:
    return [1, 2, 4, 7, 11, 15]

def test_finds_pair(sorted_nums):
    assert two_sum(sorted_nums, 15) == (2, 4)

def test_returns_none_when_no_pair(sorted_nums):
    assert two_sum(sorted_nums, 100) is None

def test_pairs_in_head(sorted_nums):
    assert two_sum(sorted_nums, 3) == (0, 1)