import re

def calculate_expression(expression: str) -> float:
    if not re.match(r'^[\d\+\-\*/\(\)\s]+$', expression):
        raise ValueError("Invalid characters in the expression.")
    
    # Evaluate the expression
    try:
        result = eval(expression)
    except Exception as e:
        raise ValueError(f"Error evaluating expression: {e}")
    
    return result

expression = "(2+3) * 2"
print(calculate_expression(expression))
