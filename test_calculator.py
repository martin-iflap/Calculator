import pytest
import calculator
from calculator import Calculator


@pytest.fixture
def calc() -> Calculator:
    return Calculator()

def test_remove_float(calc: Calculator):
    assert calc.remove_float(4.3431111,3) == 4.343
    assert calc.remove_float(4.9999,3) == 5.000
    result = calc.remove_float(4.0000, 4)
    assert result == 4
    assert isinstance(result, int)