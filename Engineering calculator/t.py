import math

class LogCalculator:
    def log_from_decimal(self, decimal_str, base=10):
        """
        Calculate the logarithm of a decimal number and return the result.

        Parameters:
        decimal_str (str): The decimal number as a string.
        base (int): The base of the logarithm (default is 10, can also be 2).

        Returns:
        float: The logarithm of the decimal number.
        """
        try:
            # Convert the decimal string to a float
            decimal_value = float(decimal_str)
            
            # Check for valid base
            if base not in [2, 10]:
                return "Invalid base. Only base 2 and base 10 are supported."
            
            # Calculate the logarithm of the decimal value
            log_value = math.log(decimal_value, base)
            
            return log_value
        except ValueError:
            return "Invalid decimal number"

# Example usage:
calculator = LogCalculator()
log_value_base10 = calculator.log_from_decimal('1234', base=10)
log_value_base2 = calculator.log_from_decimal('1234', base=2)

print(f"Logarithm in base 10: {log_value_base10}")
print(f"Logarithm in base 2: {log_value_base2}")
