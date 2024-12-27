import re
import matplotlib.pyplot as plt
from sympy import symbols, Eq, solve
from pprint import pprint

def process_input(file_path):
    """
    Process the input file and compute result1 and result2 based on the given logic.
    """
    result1 = 0
    result2 = 0
    
    robots = []
    result1_robots = []
    
    # Solution of the equation for part 2
    # entrpy of x decreases every 101 steps and entrpy of y decreases every 103 steps
    x = symbols('x')
    equation = Eq(200 + x * 101, 42 + x * 103)
    solution = solve(equation, x)
    result2 = int(solution[0]) * 101 + 200
    
    max_x, max_y = 101, 103
    with open(file_path, "r") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            nums = re.findall(r"-?\d+", line)
            robots.append(tuple(map(int, nums)))

    for j in range(8200):
        if j == 100:
            result1_robots = robots.copy()
        if j == int(solution[0]) * 101 + 200:
            x_coords = [robot[0] for robot in robots]
            y_coords = [robot[1] for robot in robots]
            plt.scatter(x_coords, y_coords)
            plt.xlabel('X Coordinate')
            plt.ylabel('Y Coordinate')
            plt.title(f'Robot Positions {j}')
            plt.grid(True)
            plt.show()
            
        for i, (x, y, dx, dy) in enumerate(robots):
            x1, y1 = x + dx, y + dy
            if x1 < 0:
                x1 = max_x + x1
            elif x1 >= max_x:
                x1 = x1 - max_x
            if y1 < 0:
                y1 = max_y + y1
            elif y1 >= max_y:
                y1 = y1 - max_y
            robots[i] = (x1, y1, dx, dy)

    def split_quadrant(max_x, max_y, robots):
        x = max_x // 2
        y = max_y // 2
        q1, q2, q3, q4 = [], [], [], []
        for robot in robots:
            if robot[0] < x and robot[1] < y:
                q1.append(robot)
            elif robot[0] > x and robot[1] < y:
                q2.append(robot)
            elif robot[0] < x and robot[1] > y:
                q3.append(robot)
            elif robot[0] > x and robot[1] > y:
                q4.append(robot)
        return len(q1) * len(q2) * len(q3) * len(q4)
    
    result1 = split_quadrant(max_x, max_y, result1_robots)
    print(result1)
    print(result2)


# Run the process on the input file
process_input("input.txt")
