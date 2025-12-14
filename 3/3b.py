with open('input.txt', 'r') as f:
    data = f.read().splitlines()

def max_in_range(l: list[int], _from: int, _to: int):
    """ max and argmax for given range """
    if _to == 0:
        _to = len(l)
    v = max(l[_from: _to])
    return v, l.index(v, _from, _to)

banks = [[int(k) for k in x] for x in data]

res = 0
for bank in banks:
    i = 0
    temp = 0
    for it in range(12):
        a, ai = max_in_range(bank, _from=i, _to=it-11)
        i = ai+1
        temp = temp*10 + a
    res += temp

print(res)