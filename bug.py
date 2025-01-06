def function_with_uncommon_error(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Error: Division by zero")
        return None
    except TypeError:
        print("Error: Unsupported operand type(s) for /'")
        return None

#Example with a common error
result1 = function_with_uncommon_error(10, 0)
print(f"Result1: {result1}")

# Example with uncommon error: using unsupported type
result2 = function_with_uncommon_error(10, "hello")
print(f"Result2: {result2}")

#Example with no error
result3 = function_with_uncommon_error(10, 2)
print(f"Result3: {result3}")