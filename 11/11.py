def process_input(file_path):
    """
    Process the input file and compute result1 and result2 based on the given logic.
    """
    result1 = 0
    result2 = 0

    all_nums = []

    def blink(num, count):
        count -= 1
        if count == 0:
            if len(str(num)) % 2 == 0:
                all_nums.append(int(str(num)[: len(str(num)) // 2]))
                all_nums.append(int(str(num)[len(str(num)) // 2 :]))
                return 2
            elif num == 0:
                all_nums.append(1)
                return 1
            else:
                all_nums.append(num * 2024)
                return 1
        elif num == 0:
            return blink(1, count)
        elif len(str(num)) % 2 == 0:
            return blink(int(str(num)[: len(str(num)) // 2]), count) + blink(
                int(str(num)[len(str(num)) // 2 :]), count
            )
        else:
            # print(num * 2024)
            return blink(num * 2024, count)

    with open(file_path, "r") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            numbers = list(map(int, line.split(" ")))

    for n in numbers:
        result1 += blink(n, 25)

    num_dict = {}
    stones_after_25 = all_nums[:]
    set_stones_after_25 = set(all_nums)
    for stone in set_stones_after_25:
        all_nums = []
        blink(stone, 25)
        num_dict[stone] = all_nums[:]
        multiplier = stones_after_25.count(stone)
        for iner_stone in num_dict[stone]:
            if iner_stone in num_dict:
                result2 += len(num_dict[iner_stone]) * multiplier
            else:
                all_nums = []
                result2 += blink(iner_stone, 25) * multiplier
                num_dict[iner_stone] = all_nums[:]

    print(result1)
    print(result2)


# Run the process on the input file
process_input("input.txt")
