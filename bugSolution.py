def function_with_uncommon_error_solution(a, b):
    if not isinstance(b, (int, float)):
        print("Error: Unsupported operand type for /, 'b' must be a number")
        return None
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Error: Division by zero")
        return None

#Example with a common error
result1 = function_with_uncommon_error_solution(10, 0)
print(f"Result1: {result1}")

# Example with uncommon error: using unsupported type
result2 = function_with_uncommon_error_solution(10, "hello")
print(f"Result2: {result2}")

#Example with no error
result3 = function_with_uncommon_error_solution(10, 2)
print(f"Result3: {result3}")

# Example with no error and float
result4 = function_with_uncommon_error_solution(10, 2.5)
print(f"Result4: {result4}") 