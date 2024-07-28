import re
def evaluate_binary_expression(expression):
# Define a helper function to convert binary to decimal
    def bin_to_dec(bin_str):
        return int(bin_str, 2)

    # Define a helper function to convert decimal to binary
    def dec_to_bin(dec_int):
        return bin(dec_int)[2:]

    # Replace binary numbers with their decimal equivalents in the expression
    def replace_binary_with_decimal(expr):
        binary_numbers = re.findall(r'[01]+', expr)
        for bin_num in binary_numbers:
            expr = expr.replace(bin_num, str(bin_to_dec(bin_num)), 1)
        return expr

    # Replace binary numbers with decimal equivalents
    decimal_expression = replace_binary_with_decimal(expression)
    
    # Evaluate the decimal expression
    try:
        result = eval(decimal_expression)
    except ZeroDivisionError:
        return "Error: Division by zero"
    except Exception as e:
        return f"Error: {e}"
    
    # Convert the result back to binary
    return dec_to_bin(result)

print(evaluate_binary_expression("1110 AND 110"))