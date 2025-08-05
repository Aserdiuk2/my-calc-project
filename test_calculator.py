import pytest
from calculator import calc

# ----------------------------------------------------------------------------------
# 1. BASIC OPERATIONS
# ----------------------------------------------------------------------------------
# Test addition, subtraction, multiplication, integer division, big integers,
# negative values, and expressions with extra whitespace.
@pytest.mark.parametrize(
    "expr, expected",
    [
        ("1 + 2", 3),                            # simple addition
        ("10 - 7", 3),                           # simple subtraction
        ("3 * 5", 15),                           # simple multiplication
        ("10 / 2", 5),                           # exact division yields int-like float
        ("123456789 * 987654321",                 # very large integer multiplication
         121932631112635269),
        ("-5 + 3", -2),                          # negative operand handling
        ("   4  *     3   ", 12),                # extra whitespace should be ignored
    ]
)
def test_basic_operations(expr, expected):
    """
    Verify that calc() correctly handles:
      - +, -, *, / on integers
      - Negative numbers
      - Arbitrary‐precision integer arithmetic
      - Whitespace in the input
    """
    result = calc(expr)
    assert result == expected, f"For '{expr}', expected {expected} but got {result}"


# ----------------------------------------------------------------------------------
# 2. FLOATING-POINT PRECISION
# ----------------------------------------------------------------------------------
def test_decimal_division():
    """
    Verify that calc() retuQQrns a Python float for non-integer division
    and that its value is approximately correct to 4 decimal places.
    """
    result = calc("7 / 3")
    # Ensure the result is a float
    assert isinstance(result, float), f"Expected float, got {type(result)}"
    # Use pytest.approx for tolerant comparison
    assert result == pytest.approx(2.3333, rel=1e-4)


# ----------------------------------------------------------------------------------
# 3. DIVISION BY ZERO HANDLING
# ----------------------------------------------------------------------------------
def test_divide_by_zero():
    """
    Verify that dividing by zero returns the specific error string.
    """
    result = calc("1 / 0")
    assert result == "Division by zero", (
        f"Expected 'Division by zero' but got '{result}'"
    )


# ----------------------------------------------------------------------------------
# 4. INVALID INPUT AND GENERAL ERROR REPORTING
# ----------------------------------------------------------------------------------
@pytest.mark.parametrize(
    "bad_expr",
    [
        "1 + * 2",   # syntax error: unexpected operator
        "foo(1)",    # NameError: 'foo' is undefined
        "",          # Empty input: SyntaxError
    ]
)
def test_invalid_input_reports_error(bad_expr):
    """
    Verify that any other error (syntax, name, empty string) produces
    a message starting with 'Error:'.
    """
    result = calc(bad_expr)
    assert isinstance(result, str), "Expected error message as string"
    assert result.startswith("Error:"), f"Expected 'Error:' prefix but got '{result}'"


# ----------------------------------------------------------------------------------
# 5. SOFTWARE LIMITS
# ----------------------------------------------------------------------------------
def test_large_integer_limit():
    """
    Test Python's arbitrary-precision integers by computing 2**10000
    and checking the result has more than 3000 digits.
    """
    large_int = calc("2**10000")
    # The result should be an integer
    assert isinstance(large_int, int)
    # Check digit count
    assert len(str(large_int)) > 3000, "Expected >3000 digits for 2**10000"


def test_float_overflow_limit():
    """
    Test floating-point overflow: multiplying a very large float by 10
    should result in 'inf'.
    """
    overflow_result = calc("1e308 * 1e10")
    # Python eval of this expression gives the special float 'inf'
    assert overflow_result == float("inf"), (
        f"Expected 'inf' but got {overflow_result}"
    )
