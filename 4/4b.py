with open("input.txt", "r") as f:
    D = [[ch for ch in row] for row in f.read().splitlines()]


res = 0
while True:

    coords = []

    for y in range(len(D)):
        for x in range(len(D[0])):
            if D[y][x] != "@":
                continue
            adj = 0
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    if dy == 0 and dx == 0:
                        continue
                    if (
                        0 <= y + dy < len(D)
                        and 0 <= x + dx < len(D[0])
                        and D[y + dy][x + dx] == "@"
                    ):
                        adj += 1
            if adj < 4:
                coords.append((y, x))

    if len(coords) == 0:
        break

    for y, x in coords:
        D[y][x] = '.'
    res += len(coords)

print(res)
