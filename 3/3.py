import re

def count_mul(temp_mull):
    pattern = r"mul\((\d+),(\d+)\)"
    match = re.fullmatch(pattern, temp_mull)
    if match:
        num1 = int(match.group(1))
        num2 = int(match.group(2))
        return num1 * num2
    else:
        return 0

def evaluate_enable(temp_enable, enable):
    if temp_enable == "don't()":
        return False
    elif temp_enable == "do()":
        return True
    else:
        return enable
        

def process_input(file_path):
    """
    Process the input file and compute result1 and result2 based on the given logic.
    """
    result1 = 0
    result2 = 0
    
    enable = True

    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            
            record_mul = False
            record_enable = False
            for ch in line:
                if record_enable:
                    temp_enable += ch
                if ch == 'd':
                    record_enable = True
                    temp_enable = 'd'
                elif ch == ')' and record_enable:
                    enable = evaluate_enable(temp_enable, enable)
                    record_enable = False
                
                if record_mul:
                    temp_mull += ch
                if ch == 'm':
                    record_mul = True
                    temp_mull = 'm'
                    continue
                elif ch == ')' and record_mul:
                    result1 += count_mul(temp_mull)
                    if enable:
                        result2 += count_mul(temp_mull)
                    record_mul = False
    print(result1)
    print(result2)          
            
# Run the process on the input file
process_input('input.txt')