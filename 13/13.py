import re
import numpy as np


def process_input(file_path):
    """
    Process the input file and compute result1 and result2 based on the given logic.
    """
    result1 = 0
    result2 = 0

    button_a = None
    button_b = None
    prize = None

    machines = []

    with open(file_path, "r") as file:
        for line in file:
            line = line.strip()
            if not line:
                machines.append(
                    (
                        (button_a[0], button_b[0], prize[0]),
                        (button_a[1], button_b[1], prize[1]),
                    )
                )
                button_a = None
                button_b = None
                prize = None
                continue

            elif not button_a:
                numbers = re.findall(r"\d+", line)
                button_a = list(map(int, numbers))
            elif not button_b:
                numbers = re.findall(r"\d+", line)
                button_b = list(map(int, numbers))
            else:
                numbers = re.findall(r"\d+", line)
                prize = list(map(int, numbers))

    def get_result(machines, extend=0):
        result = 0
        for game in machines:
            A = np.array([[game[0][0], game[0][1]], [game[1][0], game[1][1]]])
            B = np.array([extend + game[0][2], extend + game[1][2]])
            solution = np.linalg.solve(A, B)
            a, b = solution.astype(int)
            for da, db in [(0, 0), (1, 0), (0, 1)]:
                a1 = a + da
                b1 = b + db
                if all(
                    a1 * game[i][0] + b1 * game[i][1] == extend + game[i][2]
                    for i in range(2)
                ):
                    result += 3 * a1 + b1
        return result

    result1 = get_result(machines)
    result2 = get_result(machines, 10000000000000)
    print(result1)
    print(result2)


# Run the process on the input file
process_input("input.txt")
