with open("input.txt", "r") as f:
    lines = f.read().splitlines()

start = lines[0].index('S')
cache = {}

def tls(y, x):
    if (y, x) in cache:
        return cache[(y, x)]
    if y+1 == len(lines):
        ans = 1
    elif lines[y+1][x] == '^':
        ans = tls(y+1, x-1) + tls(y+1, x+1)
    else:
        ans = tls(y+1, x)
    cache[(y, x)] = ans
    return ans

print(tls(1, start))
