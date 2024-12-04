def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list
    try:
        return sum(numbers) / len(numbers)
    except ZeroDivisionError:
        return 0  # Handle division by zero