from itertools import combinations


def process_input(file_path):
    """
    Process the input file and compute result1 and result2 based on the given logic.
    """
    result1 = 0
    result2 = 0

    grid = []

    with open(file_path, "r") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue

            grid.append(list(line))

    antenas = {}
    max_x = len(grid[0])
    max_y = len(grid)
    antinodes = set()
    antinodes_part2 = set()

    for y, row in enumerate(grid):
        for x, col in enumerate(row):
            if col != ".":
                points = antenas.get(col, [])
                points.append((x, y))
                antenas[col] = points

    for ant in antenas:
        combs = list(combinations(antenas[ant], 2))
        for c in combs:
            a, b = c
            x1, y1 = a
            x2, y2 = b
            dx = x1 - x2
            dy = y1 - y2
            points = [(x1 + dx, y1 + dy), (x2 - dx, y2 - dy)]

            for x, y in points:
                if x >= 0 and x < max_x and y >= 0 and y < max_y:
                    antinodes.add((x, y))

        
        for c in combs:
            a, b = c
            x1, y1 = a
            x2, y2 = b
            dx = x1 - x2
            dy = y1 - y2
            
            antinodes_part2.add((x1, y1))
            antinodes_part2.add((x2, y2))
            while True:
                x1 += dx
                y1 += dy
                x2 -= dx
                y2 -= dy
                if ((x1 < 0 or x1 >= max_x) or (y1 < 0 or y1 >= max_y)) and ((x2 < 0 or x2 >= max_x) or (y2 < 0 or y2 >= max_y)):
                    break
                if x1 >= 0 and x1 < max_x and y1 >= 0 and y1 < max_y:
                    antinodes_part2.add((x1, y1))
                if x2 >= 0 and x2 < max_x and y2 >= 0 and y2 < max_y:
                    antinodes_part2.add((x2, y2))
                

    result1 = len(antinodes)
    result2 = len(antinodes_part2)
    print(result1)
    print(result2)


# Run the process on the input file
process_input("input.txt")
