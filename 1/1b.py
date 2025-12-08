with open('input.txt', 'r') as file:
    lines = file.read().splitlines()

pos = 50
count = 0

for ll in lines:
    dir, num = ll[0], int(ll[1:])
    neg = dir == 'L'
    if neg:
        num = -num
    npos = (pos + num)
    val = abs(npos // 100)
    npos = npos % 100
    if neg:
        if pos == 0:
            val -= 1
        if npos == 0:
            val += 1
    count += val
    pos = npos

print(count)