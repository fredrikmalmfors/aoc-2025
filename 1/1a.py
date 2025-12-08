with open('input.txt', 'r') as file:
    lines = file.read().splitlines()

pos = 50
count = 0

for ll in lines:
    dir, num = ll[0], int(ll[1:])
    if dir == 'L':
        num = -num
    pos = (pos + num) % 100
    if pos == 0:
        count += 1

print(count)
    