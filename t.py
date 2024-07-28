class HexadecimalCalculator:
    def twos_complement(self, number: str, base: int) -> str:
        
        # Convert the input number to an integer
        if base == 2:
            int_number = int(number, 2)
        elif base == 8:
            int_number = int(number, 8)
        elif base == 10:
            int_number = int(number)
        elif base == 16:
            int_number = int(number, 16)
        else:
            raise ValueError("Base must be one of 2, 8, 10, or 16")
        

        # Calculate one's complement by flipping the bits
        max_num = (1 << 64) - 1
        ones_complement_int = int_number ^ max_num

        # Calculate two's complement by adding one to the one's complement result
        twos_complement_int = ones_complement_int + 1

        # Convert back to the original base
        if base == 2:
            result = bin(twos_complement_int)[2:].zfill(64)  # Remove the '0b' prefix and pad with zeros
        elif base == 8:
            result = oct(twos_complement_int)[2:].zfill(64 // 3)  # Remove the '0o' prefix and pad with zeros
        elif base == 10:
            result = (twos_complement_int)
        elif base == 16:
            result = hex(twos_complement_int)[2:].upper().zfill(64 // 4)  # Remove the '0x' prefix and pad with zeros

        return result

def hexidecimal_to_hexidecimal_64bit_segments(hex_number):
        if not isinstance(hex_number, str):
            return "Error: Input must be a hexadecimal string."

        try:
            number = int(hex_number, 16)
        except ValueError:
            return "Error: Input must be a valid hexadecimal string."

        if number == 0:
            return ["0" * 16]  # Special case for zero, with a single 16-bit segment

        binary_result = bin(number)[2:]  # Get binary representation without '0b' prefix

        # Pad with leading zeros to make it 64 bits
        binary_result = binary_result.zfill(64)

        # Split into 16-bit segments
        segments = [binary_result[i : i + 16] for i in range(0, 64, 16)]

        return segments

def binary_tobinary_64bit_segments(binary_number):
        # Ensure the binary number is represented in 64 bits
        padded_binary = format(int(str(binary_number), 2), "064b")
        # Split the padded binary into four 16-bit chunks
        return [padded_binary[i : i + 16] for i in range(0, 64, 16)]

def decimal_to_decimal_64bit_segments(number):
        if not isinstance(number, int):
            return "Error: Input must be an integer."

        if number == 0:
            return ["0"]  # Special case for zero

        binary_result = ""
        while number > 0:
            binary_result = str(number % 2) + binary_result
            number //= 2

        # Pad with leading zeros to make it 64 bits
        binary_result = binary_result.zfill(64)

        # Split into 16-bit segments
        segments = [binary_result[i : i + 16] for i in range(0, 64, 16)]

        return segments

def octal_octal_to_64bit_segments(octal_number):
    # Convert octal to binary
    binary_string = bin(int(str(octal_number), 8))[2:]

    # Pad with leading zeros to make it 64 bits
    padded_binary = binary_string.zfill(64)

    # Split into 16-bit chunks
    chunks = [padded_binary[i : i + 16] for i in range(0, 64, 16)]

    return chunks

# Testing function
def test_twos_complement():
    calculator = HexadecimalCalculator()

    # Test cases
    test_cases = [
        ("1111", 2),  # Binary
        ("17", 8),    # Octal
        ("15", 10),   # Decimal
        ("F", 16)     # Hexadecimal
    ]

    result = calculator.twos_complement("1111", 2)
    print(f"Two's complement of {2} {result}\n")
    print(binary_tobinary_64bit_segments(result))

    result = calculator.twos_complement("17", 8)
    print(f"Two's complement of {2} {result}\n")
    print(octal_octal_to_64bit_segments(result))

    result = calculator.twos_complement("15", 10)
    print(f"Two's complement of {2} {result}\n")
    print(decimal_to_decimal_64bit_segments(result))

    result = calculator.twos_complement("F", 16)
    print(f"Two's complement of {2} {result}\n")
    print(decimal_to_decimal_64bit_segments(result))

# Run the tests
test_twos_complement()
