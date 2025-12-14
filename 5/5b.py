with open("input.txt", "r") as f:
    data = f.read().split("\n\n")[0].split("\n")

rns = [tuple(int(k) for k in x.split("-")) for x in data]
rns = list(sorted(rns, key=lambda x: (x[0], x[1])))

while True:
    rns = list(sorted(rns, key=lambda x: (x[0], x[1])))
    for i in range(len(rns) - 1):
        if rns[i][1] + 1 >= rns[i + 1][0]:
            rns[i] = (rns[i][0], max(rns[i + 1][1], rns[i][1]))
            del rns[i + 1]
            break
    else:
        break

print(sum(b - a + 1 for a, b in rns))
