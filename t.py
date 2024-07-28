def shift_left(item: str, number: str) -> str:
    # Extract the numeric part from the item string
    shift_amount = int(item.split()[0])
    
    # Convert the number string to an integer
    num = int(number)
    
    # Calculate the new number by shifting to the left
    new_number = num << shift_amount
    
    # Return the new number as a string
    return str(new_number)

# Example usage
item = "3 jegy"
number = "10"
shifted_number = shift_left(item, number)
print(shifted_number)  # Output: "7"
