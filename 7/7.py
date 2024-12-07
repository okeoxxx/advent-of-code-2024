def is_valid_sequence(test_value, numbers, part2=False):
    if len(numbers) == 1 and test_value == numbers[0]:
        return True
    elif len(numbers) == 1:
        return False
    else:
        num = numbers.pop(1)

        results = [
            [numbers[0] + num] + numbers[1:],  # Add
            [numbers[0] * num] + numbers[1:],  # Multiply
        ]
        
        if part2:
            results.append(
                [int(str(numbers[0]) + str(num))] + numbers[1:]
            )  # Concatenate

        return any(
            is_valid_sequence(test_value, result, part2=part2) for result in results
        )


def process_input(file_path):
    """
    Process the input file and compute result1 and result2 based on the given logic.
    """
    result1 = 0
    result2 = 0

    with open(file_path, "r") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            test_value, numbers = line.split(":")
            test_value = int(test_value)
            numbers = list(map(int, numbers.strip().split(" ")))
            if is_valid_sequence(test_value, numbers[:]):
                result1 += test_value
                result2 += test_value
            elif is_valid_sequence(test_value, numbers, part2=True):
                result2 += test_value

    print(result1)
    print(result2)


# Run the process on the input file
process_input("input.txt")
