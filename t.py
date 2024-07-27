def format_binary(binary_string):
    # Insert a space every four characters
    formatted_string = ' '.join(binary_string[i:i+4] for i in range(0, len(binary_string), 4))
    return formatted_string

# Example usage:
input_string = "0000000000000000"
formatted_result = format_binary(input_string)
print(formatted_result)
