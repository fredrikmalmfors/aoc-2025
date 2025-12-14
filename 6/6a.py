from dataclasses import dataclass


with open("input.txt", "r") as f:
    lines = f.read().splitlines()

grid = []
for ll in lines:
    _ll = ll.rstrip().lstrip()
    while "  " in _ll:
        _ll = _ll.replace("  ", " ")
    grid.append(_ll.split(" "))


@dataclass
class Eq:
    nums: list[int]
    op: str

    def calc(self):
        match self.op:
            case "*":
                res = 1
                for el in self.nums:
                    res = res*el
                return res
            case "+":
                return sum(self.nums)


eqs: list[Eq] = []
for x in range(len(grid[0])):
    eqs.append(
        Eq(
            nums=[int(grid[y][x]) for y in range(len(grid) - 1)], 
            op=grid[-1][x]
        )
    )

print(sum(x.calc() for x in eqs))
