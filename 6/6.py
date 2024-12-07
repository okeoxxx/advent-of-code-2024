def get_result(obstructions, visited, point, max_x, max_y):
    dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    moves = 0

    while not (
        point[0] == 0 or point[0] == max_x or point[1] == 0 or point[1] == max_y
    ):
        moves += 1
        if moves > 7000:
            return False

        next_point = (point[0] + dirs[0][0], point[1] + dirs[0][1])
        if next_point in obstructions:
            dirs.append(dirs.pop(0))
        else:
            point[0], point[1] = next_point
            visited.add((point[0], point[1]))

    return visited

def make_grid(file_path):
    grid = []
    with open(file_path, "r") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            grid.append(list(line))
    return grid

def process_input(file_path):
    """
    Process the input file and compute result1 and result2 based on the given logic.
    """
    result1 = 0
    result2 = 0

    grid = make_grid(file_path)

    obstructions = set()
    for y, row in enumerate(grid):
        for x, col in enumerate(row):
            if col == "#":
                obstructions.add((x, y))
            elif col in "^":
                point = [x, y]
                starting_position = (x, y)
    max_x = max(x for x, _ in obstructions)
    max_y = max(y for _, y in obstructions)

    visited = get_result(obstructions, {starting_position}, point[:], max_x, max_y)
    result1 = len(visited)

    visited = list(visited)
    while visited:
        test_position = visited.pop()
        if test_position == starting_position:
            continue
        obstructions.add(test_position)
        if not get_result(obstructions, {starting_position}, point[:], max_x, max_y):
            result2 += 1
        obstructions.remove(test_position)

    print(result1)
    print(result2)


# Run the process on the input file
process_input("input.txt")
