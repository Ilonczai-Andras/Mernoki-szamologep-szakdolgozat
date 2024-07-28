import re

def evaluate_hex_expression(expression):
    # Regular expression to find hexadecimal numbers (e.g., A, FF)
    hex_pattern = re.compile(r'\b[0-9a-fA-F]+\b')

    # Function to convert hexadecimal to decimal
    def hex_to_dec(match):
        return str(int(match.group(), 16))

    # Replace all hexadecimal numbers in the expression with their decimal equivalents
    decimal_expression = hex_pattern.sub(hex_to_dec, expression)

    try:
        # Evaluate the decimal expression
        result = eval(decimal_expression)
    except Exception as e:
        return f"Error evaluating expression: {e}"

    return result

# Example usage
expression = "A +FF * (3+4)"
result = evaluate_hex_expression(expression)
print(f"Result of the expression '{expression}' is: {result}")
