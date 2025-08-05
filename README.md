# Simple Calculator

A lightweight Python library for evaluating basic arithmetic expressions with support for addition, subtraction, multiplication, integer division, big integers, negative numbers, and flexible whitespace handling.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Running Tests](#running-tests)

## Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/<YOUR_USERNAME>/<REPO_NAME>.git
cd <REPO_NAME>
python -m venv venv
source venv/bin/activate   # on Windows use `venv\Scripts\activate`
pip install pytest
```

## Usage

Import and call the `calc` function in your code:

```python
from calc import calc

# Basic expressions
a = calc("1 + 2")          # => 3
b = calc("10 / 2")         # => 5
c = calc("123456789*987654321")  # => 121932631112635269
\# Handle whitespace and negatives
d = calc("  -5  +   3 ")     # => -2
print(a, b, c, d)
```

## Running Tests

This project uses pytest. Run the full test suite with:

```bash
pytest -v
```

You should see output like:

```                                                       
========================================== test session starts =====================================================================
platform win32 -- Python 3.12.0, pytest-8.4.1, pluggy-1.6.0 -- C:\Users\PC\PycharmProjects\NewTestProject\.venv\Scripts\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\PC\PycharmProjects\NewTestProject
collected 14 items                                                                                                                                                                                      

test_calculator.py::test_basic_operations[1 + 2-3] PASSED                                                                                                                                         [  7%]
test_calculator.py::test_basic_operations[10 - 7-3] PASSED                                                                                                                                        [ 14%]
test_calculator.py::test_basic_operations[3 * 5-15] PASSED                                                                                                                                        [ 21%]
test_calculator.py::test_basic_operations[10 / 2-5] PASSED                                                                                                                                        [ 28%]
test_calculator.py::test_basic_operations[123456789 * 987654321-121932631112635269] PASSED                                                                                                        [ 35%]
test_calculator.py::test_basic_operations[-5 + 3--2] PASSED                                                                                                                                       [ 42%]
test_calculator.py::test_basic_operations[   4  *     3   -12] PASSED                                                                                                                             [ 50%]
test_calculator.py::test_decimal_division PASSED                                                                                                                                                  [ 57%]
test_calculator.py::test_divide_by_zero PASSED                                                                                                                                                    [ 64%]
test_calculator.py::test_invalid_input_reports_error[1 + * 2] PASSED                                                                                                                              [ 71%]
test_calculator.py::test_invalid_input_reports_error[foo(1)] PASSED                                                                                                                               [ 78%]
test_calculator.py::test_invalid_input_reports_error[] PASSED                                                                                                                                     [ 85%]
test_calculator.py::test_large_integer_limit PASSED                                                                                                                                               [ 92%]
test_calculator.py::test_float_overflow_limit PASSED                                                                                                                                              [100%]

========================================== 14 passed in 0.03s =======================================================================


```
