def process_input(file_path):
    """
    Process the input file and compute result1 and result2 based on the given logic.
    """
    result1 = 0
    result2 = 0

    disk_map = ""

    with open(file_path, "r") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            disk_map = line
    #disk_map = "2333133121414131402"
    list_num = []
    list_gap = []
    for i, num in enumerate(disk_map):
        if i % 2 == 0:
            list_num.append(int(num))
        else:
            list_gap.append(int(num))
    list_num2 = list_num[:]
    list_gap2 = list_gap[:]
    temp_end = []
    id = 0
    for j, n in enumerate(list_num):
        for number in [j] * n:
            result1 += id * number
            id += 1

        for _ in range(list_gap.pop(0)):
            if not temp_end:
                num = list_num.pop()
                if j == len(list_num):
                    break
                temp_end = [len(list_num)] * num

            n1 = temp_end.pop()
            result1 += id * n1
            id += 1

    while temp_end:
        n1 = temp_end.pop()
        result1 += id * n1
        id += 1

    start_num_index = []
    start_gap_index = []
    disk = []
    for i, num in enumerate(list_num2):
        start_num_index.append(len(disk))
        disk += [i] * num
        
        try:
            if list_gap2[i] > 0:
                start_gap_index.append(len(disk))
            for _ in range(list_gap2[i]):
                disk.append(".")
        except:
            pass
    
    def set_gap(disk):
        list_gap, start_gap_index = [], []
        i = 0
        n = len(disk)
        while i < n:
            if disk[i] == ".":
                start_gap_index.append(i)
                count = 0
                while i < n and disk[i] == ".":
                    count += 1
                    i += 1
                list_gap.append(count)
            else:
                i += 1
        return list_gap[:-1], start_gap_index

    while list_num2:
        num = list_num2.pop()
        for i, gap in enumerate(list_gap2):
            if num <= gap:
                for j in range(num):
                    src = start_num_index[len(list_num2)] + j
                    dest = start_gap_index[i] + j
                    if dest < src:
                        disk[dest] = len(list_num2)
                        disk[src] = "."
                list_gap2[i] -= num
                start_gap_index[i] += num

                list_gap2, start_gap_index = set_gap(disk)
                break

    for i, num in enumerate(disk):
        if num != ".":
            result2 += num * i
    print(result1)
    print(result2)


# Run the process on the input file
process_input("input.txt")
