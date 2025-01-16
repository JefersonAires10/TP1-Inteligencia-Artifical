class Estado:
    def __init__(self, x, y, profundidade=0, cost=0):
        self.x = x
        self.y = y
        self.profundidade = profundidade
        self.cost = cost

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

    def __repr__(self):
        return f"({self.x}, {self.y}, {self.profundidade}, {self.cost})"