def float_to_octal2(f):
    """
    Convert a floating-point number to its octal representation as a string.
    
    Parameters:
    f (float): The floating-point number to convert.
    
    Returns:
    str: The octal representation of the floating-point number.
    """
    if f < 0:
        sign = "-"
        f = -f
    else:
        sign = ""

    # Separate the integer part and the fractional part
    integer_part = int(f)
    fractional_part = f - integer_part
    
    # Convert the integer part to octal
    octal_integer = oct(integer_part)[2:]

    # Convert the fractional part to octal
    octal_fraction = ""
    while fractional_part != 0 and len(octal_fraction) < 12:  # limit length to prevent infinite loop
        fractional_part *= 8
        digit = int(fractional_part)
        octal_fraction += str(digit)
        fractional_part -= digit

    return sign + octal_integer + ("." + octal_fraction if octal_fraction else "")

def power_octal(octal_str, power_value):
    """
    Calculate the result of raising an octal number to a given power and return the result as an octal string.

    Parameters:
    octal_str (str): The octal number as a string.
    power_value (float): The power to which the octal number is to be raised.

    Returns:
    str: The octal representation of the result after exponentiation.
    """
    try:
        # Convert the octal string to a decimal number
        decimal_value = int(octal_str, 8)
        
        # Perform the power operation
        result_value = decimal_value ** power_value
        
        # Convert the result back to an octal string with fraction handling
        octal_result = float_to_octal2(result_value)
        
        return octal_result
    except ValueError as e:
        return f"Error: {e}"

# Example usage:
octal_number = "77"  # Octal number
power_value = -1  # Power value
result = power_octal(octal_number, power_value)
print(f"The result of {octal_number} raised to the power of {power_value} is: {result}")

power_value = -2  # Power value
result = power_octal(octal_number, power_value)
print(f"The result of {octal_number} raised to the power of {power_value} is: {result}")
