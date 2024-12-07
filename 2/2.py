def is_valid_sequence(numbers):
    """
    Check if the given list of numbers satisfies the condition:
    Consecutive numbers differ by 1, 2, or 3.
    """
    current = numbers.pop()
    while numbers:
        next_number = numbers.pop()
        if 0 < next_number - current < 4:
            current = next_number
        else:
            break
        if not numbers:
            return True
    return False

def process_input(file_path):
    """
    Process the input file and compute result1 and result2 based on the given logic.
    """
    result1 = 0
    result2 = 0

    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if not line:
                continue

            # Parse numbers from the line and create forward and reversed lists
            numbers = list(map(int, line.split()))

            # Check the original and reversed lists for validity
            if is_valid_sequence(numbers[:]) or is_valid_sequence(numbers[::-1]):
                result1 += 1
                result2 += 1
            else:
                # Attempt to remove one number at a time and check validity
                for i in range(len(numbers)):
                    modified_numbers = numbers[:i] + numbers[i+1:]
                    if is_valid_sequence(modified_numbers[:]) or is_valid_sequence(modified_numbers[::-1]):
                        result2 += 1
                        break

    print(result1)
    print(result2)

# Run the process on the input file
process_input('input.txt')
