with open("input.txt", "r") as f:
    data = f.read().split('\n\n')

ranges, ids = [x.split('\n') for x in data]
ranges = [tuple(int(k) for k in x.split('-')) for x in ranges]
ids = [int(x) for x in ids]

res = 0
for id in ids:
    for a, b in ranges:
        if a <= id <= b:
            res += 1
            break

print(res)