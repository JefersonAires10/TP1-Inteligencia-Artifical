import random
class Node:
    def __init__(self, x, y, custo, profundidade, pai=None, acao_custo=None):
        self.x = x
        self.y = y
        self.custo = custo
        self.profundidade = profundidade
        self.pai = pai
        self.acao_custo = acao_custo

    def __lt__(self, other):
        return self.custo < other.custo

    def gerar_vizinhos(self, visitados):
        x, y, profundidade = self.x, self.y, self.profundidade
        vizinhos = []
        estados_vizinhos = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
        acoes = ["f1", "f2", "f3", "f4"] # Mapeando vizinhos com ações
        random.shuffle(estados_vizinhos)
    
        for i, (nx, ny) in enumerate(estados_vizinhos):
            if nx >= 0 and ny >= 0 and (nx, ny) not in visitados:
                vizinho = Node(nx, ny, 0, profundidade + 1, self)
                # Ajuste: Passar a acao para função de custo
                custo_novo = self.custo + self.acao_custo(acoes[i], profundidade)
                vizinho.custo = custo_novo
                vizinho.acao_custo = self.acao_custo
                vizinhos.append(vizinho)
        print(f"Vizinhos gerados para ({self.x}, {self.y}): {[ (v.x, v.y) for v in vizinhos ]}")
        return vizinhos
    
def reconstruir_caminho(no):
    caminho = []
    while no:
        caminho.append((no.x, no.y))
        no = no.pai
    return list(reversed(caminho))
