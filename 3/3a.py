with open('input.txt', 'r') as f:
    data = f.read().splitlines()

def max_in_range(l: list[int], _from: int = 0, _to: int | None = None):
    if _to is None:
        _to = len(l)
    v = max(l[_from: _to])
    return v, l.index(v, _from, _to)

banks = [[int(k) for k in x] for x in data]

res = 0
for bank in banks:
    a, ai = max_in_range(bank, _to=-1)
    b, _ = max_in_range(bank, _from=ai+1)
    res += a*10 + b

print(res)