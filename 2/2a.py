with open('input.txt', 'r') as f:
    data = f.read().split(',')

res = 0

for dd in data:
    start, end = dd.split('-')
    rans = [start]
    for p in range(len(start), len(end)):
        rans += [str(10**p-1), str(10**p)]
    rans += [end]
    rans = [x for x in rans if len(str(x)) % 2 == 0]
    if not rans:
        continue
    assert len(rans) == 2
    r1, r2 = rans
    hs = len(str(r1)) // 2
    for part in range(int(r1[:hs]), int(r2[:hs])+1):
        check = int(f'{part}{part}')
        if int(r1) <= check <= int(r2):
            res += check

print(res)


