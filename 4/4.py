def process_input(file_path):
    """
    Process the input file and compute result1 and result2 based on the given logic.
    """
    result1 = 0
    result2 = 0
    
    word = 'XMAS'
    grid = []
    dirs = [(1,0), (1,1), (0,1), (-1,1), (-1,0), (-1,-1), (0,-1),(1,-1)]
    diagonals = [((1,1), (-1,-1)), ((-1,1), (1,-1))]

    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            grid.append(list(line))
        
        for y1, row in enumerate(grid):
            for x1, col in enumerate(row):
                if col == 'X':
                    for dir in dirs:
                        for i in [3, 2, 1]:
                            x2 = (dir[0] * i) + x1
                            y2 = (dir[1] * i) + y1
                            if i == 3 and (0 > x2 or x2 >= len(row) or 0 > y2 or y2 >= len(grid)):
                                break
                            elif grid[y2][x2] != word[i]:
                                break
                            elif i == 1:
                                result1 += 1
        
        for y1, row in enumerate(grid[:-1]):
            for x1, col in enumerate(row[:-1]):
                if x1 == 0 or y1 == 0:
                    continue
                elif col == 'A':
                    matches = 0 
                    for d in diagonals:
                        x2, y2 = d[0][0] + x1, d[0][1] + y1
                        x3, y3 = d[1][0] + x1, d[1][1] + y1
                        if (grid[y2][x2] == 'M' and grid[y3][x3] == 'S') or (grid[y2][x2] == 'S' and grid[y3][x3] == 'M'):
                            matches += 1
                            if matches == 2:
                                result2 += 1
                                
    print(result1)
    print(result2)          
            
# Run the process on the input file
process_input('input.txt')