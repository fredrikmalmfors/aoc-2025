from dataclasses import dataclass
from enum import Enum
from itertools import combinations


with open(f"input.txt", "r") as f:
    lines = f.read().splitlines()


@dataclass(frozen=True)
class Point:
    y: int
    x: int


class Dir(Enum):
    RIGHT = 0
    DOWN = 1
    LEFT = 2
    UP = 3


@dataclass
class Spinnor:

    current: Dir = Dir.RIGHT
    spin_count: int = 0

    def turn(self, _next: Dir) -> int:
        delta = (_next.value - self.current.value) % 4
        assert delta in [1, 3], "Bad turn"
        self.spin_count += 1 if delta == 1 else -1
        self.current = _next


REDS = tuple(Point(int(x.split(",")[1]), int(x.split(",")[0])) for x in lines)
GREENS: set[Point] = set()
BOMBS: set[Point] = set()
SPINNOR = Spinnor()

# This loop
# - Places Red and Green tiles
# - Places BOMBS just outside of the border
# - Keeps track of accumulated spin
for i, p in enumerate(REDS):
    np = REDS[(i + 1) % len(REDS)]
    
    if p.x == np.x:
        direction = Dir.DOWN if np.y > p.y else Dir.UP
        l, u = min(p.y + 1, np.y), max(p.y + 1, np.y)
        for dy in range(l, u):
            GREENS.add(Point(dy, p.x))
            BOMBS.add(Point(dy, p.x + (1 if np.y > p.y else -1)))
    if p.y == np.y:
        direction = Dir.RIGHT if np.x > p.x else Dir.LEFT
        l, u = min(p.x + 1, np.x), max(p.x + 1, np.x)
        for dx in range(l, u):
            GREENS.add(Point(p.y, dx))
            BOMBS.add(Point(p.y + (-1 if np.x > p.x else 1), dx))

    SPINNOR.turn(direction)

assert SPINNOR.spin_count == 4  # Asserts ONE(!) clockwise loop

# This removes wrongly places bombs
BOMBS = BOMBS - GREENS
BOMBS = BOMBS - set(REDS)

max_area = 0
for pa, pb in combinations(REDS, 2):
    area = (abs(pa.y - pb.y) + 1) * (abs(pa.x - pb.x) + 1)
    if area < max_area:
        continue

    # If there are BOMBS in the area, that means we are outside of the red+green tiles
    if any(
        min(pa.y, pb.y) <= bomb.y <= max(pa.y, pb.y)
        and min(pa.x, pb.x) <= bomb.x <= max(pa.x, pb.x)
        for bomb in BOMBS
    ):
        continue
    max_area = area

print(max_area)
assert max_area == 1573359081
