import random


class Puzzle:
    def __init__(self):
        self._q = ""
        self._a = 0

    def generate(self):
        pass

    def question(self):
        return self._q

    def check(self, txt):
        txt = txt.strip()
        if txt == "":
            return False
        try:
            return int(txt) == self._a
        except ValueError:
            return False
    
    def __str__(self):
        return f"{self._q} (answer={self._a})"

class MathPuzzle(Puzzle):
    def __init__(self, op):
        super().__init__()
        self.op = op

    def generate(self):
        if self.op == "+":
            a, b = random.randint(0, 100), random.randint(0, 100)
            self._q, self._a = f"{a} + {b} = ?", a + b
        elif self.op == "-":
            a, b = random.randint(0, 100), random.randint(0, 100)
            if b > a:
                a, b = b, a
            self._q, self._a = f"{a} - {b} = ?", a - b
        elif self.op == "*":
            a, b = random.randint(0, 12), random.randint(0, 12)
            self._q, self._a = f"{a} * {b} = ?", a * b
        else:
            d = random.randint(1, 12)
            r = random.randint(0, 12)
            n = d * r
            self._q, self._a = f"{n} / {d} = ?", r


def new_puzzle():
    p = MathPuzzle(random.choice(["+", "-", "*", "/"]))
    p.generate()
    return p