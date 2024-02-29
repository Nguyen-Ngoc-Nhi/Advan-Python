import math

def truncate_decimal_to_1_digit(number):
    # Truncate the decimal part to 1 digit after the decimal point
    truncated_number = math.floor(number * 10) / 10
    
    return truncated_number

# Example usage:
decimal_number = 12.456
truncated_number = truncate_decimal_to_1_digit(decimal_number)
print("Original number:", decimal_number)
print("Number truncated to 1 decimal place:", truncated_number)
