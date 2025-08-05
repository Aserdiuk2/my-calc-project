# Simple Calculator

A lightweight Python library for evaluating basic arithmetic expressions with support for addition, subtraction, multiplication, integer division, big integers, negative numbers, and flexible whitespace handling.

## Table of Contents

* [[Installation]
* [[Usage]
* [[Running Tests]

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
collected 7 items

test_calc.py ....... [100%]

7 passed in 0.05s
```
