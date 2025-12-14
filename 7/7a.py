with open("input.txt", "r") as f:
    lines = f.read().splitlines()

X = set([lines[0].index('S')])
count = 0
for ll in lines[1:]:
    if all(ch == '.' for ch in ll):
        continue
    NX = set()
    for x in X:
        if ll[x] == '^':
            NX.add(x+1)
            NX.add(x-1)
            count += 1
        else:
            NX.add(x)
    X = NX

print(count)
