# Function to divide two numbers
def divide_numbers(a, b):
    try:
        # Try to perform the division
        result = a / b
    except ZeroDivisionError as e:
        # Handle the error if division by zero is attempted
        print(f"Error: Cannot divide by zero. ({e})")
        result = None
    except TypeError as e:
        # Handle the error if incorrect types are used
        print(f"Error: Invalid input types. ({e})")
        result = None
    else:
        # Executed if no exception occurs
        print("Division successful.")
    finally:
        # Always executed regardless of exceptions
        print("Execution of divide_numbers completed.")
    
    return result

# Test cases
print(divide_numbers(10, 2))   # Should print the result of the division
print(divide_numbers(10, 0))   # Should print an error message for division by zero
print(divide_numbers(10, "a")) # Should print an error message for invalid types
