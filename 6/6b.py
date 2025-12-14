from dataclasses import dataclass


with open("input.txt", "r") as f:
    lines = f.read().splitlines()

@dataclass
class Eq:
    nums: list[int]
    op: str | None = None

    def calc(self):
        match self.op:
            case "*":
                res = 1
                for el in self.nums:
                    res = res*el
                return res
            case "+":
                return sum(self.nums)

H = len(lines) - 1

eqs = [Eq([])]

for x in range(len(lines[0]) -1, -1, -1):
    val = "".join(lines[y][x] for y in range(H))
    if val == ' ' * H:
        eqs.append(Eq([]))
        continue
    eqs[-1].nums.append(int(val))
    op = lines[H][x]
    if op != ' ':
        eqs[-1].op = op

print(sum(x.calc() for x in eqs))
