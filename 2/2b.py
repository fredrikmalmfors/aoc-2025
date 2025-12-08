with open('input.txt', 'r') as f:
    data = f.read().split(',')

res = set()

for dd in data:
    start, end = dd.split('-')
    rans = [start]
    for p in range(len(start), len(end)):
        rans += [str(10**p-1), str(10**p)]
    rans += [end]
    if not rans:
        continue
    assert len(rans) % 2 == 0
    rans = [x for x in rans if len(x) > 1]
    pairs = [(rans[2*i], rans[2*i+1]) for i in range(len(rans)//2)]
    for a, b in pairs:
        hs = len(a) // 2
        for i in range(1, hs+1):
            if len(a) % i != 0:
                continue
            mul = len(a) // i
            for part in range(int(a[:i]), int(b[:i])+1):
                check = int(str(part) * mul)
                if int(a) <= check <= int(b):
                    res.add(check)

print(sum(res))


