import pytest
import calculator
from calculator import Calculator


@pytest.fixture
def calc() -> Calculator:
    return Calculator()

def create_operation(calc: Calculator,
                     n1: int,
                     operator: str,
                     n2: int,
                     invert_first: bool,
                     invert_second: bool) -> None:
    """Operation helper function"""
    calc.num_click(n1)
    if invert_first:
        calc.invert()
    calc.operator_click(operator)
    calc.num_click(n2)
    if invert_second:
        calc.invert()
    calc.operator_click("=")


def test_remove_float(calc: Calculator) -> None:
    """Test remove float function"""
    assert calc.remove_float(4.3431111,3) == 4.343
    assert calc.remove_float(4.9999,3) == 5.000
    result = calc.remove_float(4.0000, 4)
    assert result == 4
    assert isinstance(result, int)

def test_plus(calc: Calculator) -> None:
    """Test addition"""
    create_operation(calc, 5, "+", 4, False, False)
    assert calc.result_string.get() == "9"

def test_plus_negative(calc: Calculator) -> None:
    """Test negative number addition"""
    create_operation(calc, 5, "+", 4, False, True)
    assert calc.result_string.get() == "1"
# negative plus negative
    calc.display_num = []
    create_operation(calc, 6, "+", 4, True, True)
    assert calc.result_string.get() == "-10"

def test_minus(calc: Calculator) -> None:
    """Test subtraction"""
    create_operation(calc, 5, "-", 4, False, False)
    assert calc.result_string.get() == "1"

def test_minus_negative(calc: Calculator) -> None:
    """Test negative number subtraction"""
    create_operation(calc, 6, "-", 4, False, True)
    assert calc.result_string.get() == "10"
# negative minus negative
    calc.display_num = []
    create_operation(calc, 6, "-", 4, True, True)
    assert calc.result_string.get() == "-2"

def test_multiplication(calc: Calculator) -> None:
    """Test multiplication"""
    create_operation(calc, 5, "*", 5, False, False)
    assert calc.result_string.get() == "25"

def test_multiply_negative(calc: Calculator) -> None:
    """Test negative number multiplication"""
    create_operation(calc, 5, "*", 5, False, True)
    assert calc.result_string.get() == "-25"
# negative times negative
    calc.display_num = []
    create_operation(calc, 5, "*", 5, True, True)
    assert calc.result_string.get() == "25"

def test_division(calc: Calculator) -> None:
    """Test division"""
    create_operation(calc, 30, "/", 5, False, False)
    assert calc.result_string.get() == "6"

def test_divide_negative(calc: Calculator) -> None:
    """Test negative number division"""
    create_operation(calc, 30, "/", 5, False, True)
    assert calc.result_string.get() == "-6"
# negative divided by negative
    calc.display_num = []
    create_operation(calc, 30, "/", 5, True, True)
    assert calc.result_string.get() == "6"

def test_zero_division(calc: Calculator) -> None:
    """Test division by zero"""
    create_operation(calc, 30, "/", 0, False, False)
    assert calc.result_string.get() == "Error"
    assert calc.full_operation == []
    assert calc.display_num == []

def test_invert(calc: Calculator) -> None:
    """Test invert function"""
    calc.num_click(5)
    calc.invert()
    assert calc.result_string.get() == "-5"
    calc.invert()
    assert calc.result_string.get() == "5"

def test_percent_relative(calc: Calculator) -> None:
    """Test percent function"""
    calc.num_click(50)
    calc.operator_click("+")
    calc.num_click(10)
    calc.percent()
    assert calc.result_string.get() == "10%"
    calc.operator_click("=")
    assert calc.result_string.get() == "55"

def test_percent_alone(calc: Calculator) -> None:
    """Test percent function without preceding number"""
    calc.num_click(100)
    calc.percent()
    assert calc.result_string.get() == "1"
    calc.percent()
    assert calc.result_string.get() == "0.01"

