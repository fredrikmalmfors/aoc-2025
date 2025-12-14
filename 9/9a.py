with open("input.txt", "r") as f:
    lines = f.read().splitlines()

D = [tuple(int(ch) for ch in x.split(",")) for x in lines]

ans = 0
for (ya, xa) in D:
    for (yb, xb) in D:
        area = (abs(ya - yb) + 1) * (abs(xa - xb) + 1)
        ans = max(ans, area)

print(ans)