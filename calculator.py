def calc(expr: str):
    """
    Evaluate a simple arithmetic expression passed as a string.
    Returns:
      - The numeric result (int or float) for valid expressions.
      - The string "Division by zero" if a ZeroDivisionError occurs.
      - The string "Error: <message>" for any other exception.
    """
    try:
        # Use Python's eval to compute the expression
        return eval(expr)
    except ZeroDivisionError:
        # Handle division by zero separately
        return "Division by zero"
    except Exception as e:
        # Catch all other errors (syntax, name errors, etc.)
        return f"Error: {e}"

