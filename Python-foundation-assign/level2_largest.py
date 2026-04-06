def find_largest(numbers):
    """
    Return the largest number in a list.
    """
    if not numbers:
        return None

    largest = numbers[0]

    for num in numbers:
        if num > largest:
            largest = num

    return largest


numbers = list(map(int, input("Enter numbers separated by space: ").split()))
print("Largest number:", find_largest(numbers))