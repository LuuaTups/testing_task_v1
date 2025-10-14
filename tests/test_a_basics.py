import math
import pytest
from src.a_basics import (
    add, sub, mul, div, sum_list, is_even, factorial, reverse_string,
    is_palindrome, to_title_case, clamp, median, unique_letters
)

# A-OSA TESTID: Kirjuta teste, et leida vigased funktsioonid!
# Järgmised 2 testi on näited - kirjuta ülejäänud testid ise!

def test_add_basic():
    """Test liitmise funktsiooni."""
    assert add(2, 3) == 5
    assert add(0, 0) == 0
    assert add(-1, 1) == 0
    assert add(-2, -3) == -5

def test_sub_basic():
    """Test lahutamise funktsiooni."""
    assert sub(10, 7) == 3
    assert sub(5, 3) == 2
    assert sub(0, 5) == -5


