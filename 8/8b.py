from dataclasses import dataclass

with open("input.txt", "r") as f:
    lines = f.read().splitlines()


@dataclass(frozen=True)
class Box:
    x: int
    y: int
    z: int

def eucl(a: Box, b: Box):
    return sum(abs(getattr(a, o) - getattr(b, o)) ** 2 for o in ["x", "y", "z"])

def fbox(a: Box, b: Box):
    return frozenset((a, b))


B: list[Box] = [Box(*[int(c) for c in coords.split(",")]) for coords in lines]
D: dict[frozenset[Box], int] = {}
C: list[set[Box]] = [set([x]) for x in B]

for a in B:
    for b in B:
        if a is b:
            continue
        if fbox(a, b) in D:
            continue
        dist = eucl(a, b)
        D[fbox(a, b)] = dist

for k, dist in sorted(D.items(), key= lambda x: x[1]):
    a, b = k
    
    # connect A to B
    ai = None
    bi = None
    for i, c in enumerate(C):
        if a in c:
            ai = i
        if b in c:
            bi = i

    assert ai is not None
    assert bi is not None

    if ai != bi:
        C[ai] = C[ai].union(C[bi])
        del C[bi]

    if len(C) == 1:
        print(a.x * b.x)
        break