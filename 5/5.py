def check_updates(update, rules, fixer=False):
    for num in update:
        for rule in rules:
            if num in rule and rule[0] in update and rule[1] in update:
                index1 = update.index(rule[0])
                index2 = update.index(rule[1])
                if index1 > index2:
                    if not fixer:
                        return 0
                    else:
                        update[index1], update[index2] = update[index2], update[index1]
                        return check_updates(update, rules, fixer=True)    
    return update[len(update)//2]

def parse_file(file_path):
    rules = []
    updates = []
    trigger = False

    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if not line:
                trigger = True
                continue
            if not trigger:
                rules.append(tuple(map(int, line.split('|'))))
            else:
                updates.append(list(map(int, line.split(','))))
    return updates, rules

def process_input(file_path):
    """
    Process the input file and compute result1 and result2 based on the given logic.
    """
    result1 = 0
    result2 = 0
    updates, rules = parse_file(file_path)
    
    for u in updates:
        result = check_updates(u, rules)
        if result:
            result1 += result
        else:
            result2 += check_updates(u, rules, fixer=True)
    print(result1)
    print(result2)
# Run the process on the input file
process_input('input.txt')
