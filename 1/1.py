data1 = []
data2 = []
with open('input.txt', 'r') as f:
    while True:
        line = f.readline().strip()
        if line == '':
            break
        a, b = map(int, line.split('   '))
        data1.append(a)
        data2.append(b)
        
    data1.sort()
    data2.sort()
    
    numbers = {}
    for num in data2:
        numbers[num] = data2.count(num)
        
    sum = 0
    sum2 = 0
    
    while data1:
        a = data1.pop()
        b = data2.pop()
        sum += abs(a-b)
        
        sum2 += a * numbers.get(a, 0)
        
    print(sum)
    print(sum2)
