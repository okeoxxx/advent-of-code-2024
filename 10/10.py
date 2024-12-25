def process_input(file_path):
    """
    Process the input file and compute result1 and result2 based on the given logic.
    """
    result1 = 0
    result2 = 0

    topo_map = []

    with open(file_path, "r") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            topo_map.append(list(map(int, list(line))))

    dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))

    all_trails = []
    trailheads = {}

    def check_trails(path):
        x1, y1 = path[-1]
        for dx, dy in dirs:
            x2 = x1 + dx
            y2 = y1 + dy
            if 0 <= x2 < len(topo_map[0]) and 0 <= y2 < len(topo_map):
                if len(path) == 9 and topo_map[y2][x2] == len(path):
                    new_path = path[:] + [(x2, y2)]
                    all_trails.append(new_path)
                    trailhead = trailheads.get(path[0], set())
                    trailhead.add((x2, y2))
                    trailheads[path[0]] = trailhead
                elif topo_map[y2][x2] == len(path):
                    new_path = path[:] + [(x2, y2)]
                    check_trails(new_path)
                else:
                    continue
            else:
                continue

    for y, row in enumerate(topo_map):
        for x, num in enumerate(row):
            if num == 0:
                check_trails([(x, y)])
    for trailhead in trailheads:
        result1 += len(trailheads[trailhead])

    result2 = len(all_trails)
    print(result1)
    print(result2)


# Run the process on the input file
process_input("input.txt")
