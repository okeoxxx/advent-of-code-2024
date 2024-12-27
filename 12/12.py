from collections import deque


def find_clusters(data):
    clusters = {}

    for char, points in data.items():
        visited = set()
        components = []

        def bfs(start):
            queue = deque([start])
            cluster = []
            while queue:
                x, y = queue.popleft()
                if (x, y) in visited:
                    continue
                visited.add((x, y))
                cluster.append((x, y))
                # Check all four possible neighbors
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    neighbor = (x + dx, y + dy)
                    if neighbor in points and neighbor not in visited:
                        queue.append(neighbor)
            return cluster

        # Traverse all points and find clusters
        for point in points.keys():
            if point not in visited:
                components.append(bfs(point))

        clusters[char] = components

    return clusters


def process_input(file_path):
    """
    Process the input file and compute result1 and result2 based on the given logic.
    """
    result1 = 0
    result2 = 0

    grid = []
    fields = {}

    with open(file_path, "r") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            grid.append(list(line))

    for y, row in enumerate(grid):
        for x, field in enumerate(row):
            perimeter = 0
            points = fields.get(field, {})
            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                x2 = x + dx
                y2 = y + dy
                if 0 <= x2 < len(grid[0]) and 0 <= y2 < len(grid):
                    if grid[y2][x2] != field:
                        perimeter += 1
                else:
                    perimeter += 1
            points[(x, y)] = perimeter
            fields[field] = points

    clusters = find_clusters(fields)

    conditions = [
        ((0, 1), (1, 1), (1, 0)),
        ((0, -1), (1, -1), (1, 0)),
        ((0, -1), (-1, -1), (-1, 0)),
        ((0, 1), (-1, 1), (-1, 0)),
    ]

    for char, components in clusters.items():
        for component in components:
            perimeter = 0
            vectres = 0
            for point in component:
                perimeter += fields[char][point]
                x, y = point
                for con in conditions:
                    da, db, dc = con
                    a = (x + da[0], y + da[1])
                    b = (x + db[0], y + db[1])
                    c = (x + dc[0], y + dc[1])
                    if a in component and b not in component and c in component:
                        vectres += 1
                    elif a not in component and c not in component:
                        vectres += 1
            result1 += len(component) * perimeter
            result2 += len(component) * vectres

    print(result1)
    print(result2)


# Run the process on the input file
process_input("input.txt")
