from collections import deque
import heapq
import math

# Classe para representar um nó na árvore de busca
class Node:
    def __init__(self, x, y, custo, profundidade, pai=None):
        self.x = x
        self.y = y
        self.custo = custo
        self.profundidade = profundidade
        self.pai = pai  # Para reconstruir o caminho

    def __lt__(self, other):
        return self.custo < other.custo

# Função para reconstruir o caminho
def reconstruir_caminho(no):
    caminho = []
    while no:
        caminho.append((no.x, no.y))
        no = no.pai
    return list(reversed(caminho))

# Função para gerar os vizinhos de um nó
def gerar_vizinhos(no, acaoCusto):
    x, y, profundidade = no.x, no.y, no.profundidade
    vizinhos = [
        Node(x - 1, y, no.custo + acaoCusto("f1", profundidade), profundidade + 1, no),  # Esquerda
        Node(x + 1, y, no.custo + acaoCusto("f2", profundidade), profundidade + 1, no),  # Direita
        Node(x, y - 1, no.custo + acaoCusto("f3", profundidade), profundidade + 1, no),  # Baixo
        Node(x, y + 1, no.custo + acaoCusto("f4", profundidade), profundidade + 1, no),  # Cima
    ]
    return [vizinho for vizinho in vizinhos if vizinho.x >= 0 and vizinho.y >= 0]

# Implementação dos algoritmos
def busca_em_largura(x1, y1, x2, y2, acaoCusto):
    fila = deque([Node(x1, y1, 0, 0)])
    visitados = set()
    nos_gerados = 0

    while fila:
        no_atual = fila.popleft()
        estado_atual = (no_atual.x, no_atual.y)

        if estado_atual == (x2, y2):
            return {
                "estado_inicial": (x1, y1),
                "objetivo": (x2, y2),
                "caminho": reconstruir_caminho(no_atual),
                "custo": no_atual.custo,
                "nos_gerados": nos_gerados,
                "nos_visitados": len(visitados),
            }

        if estado_atual not in visitados:
            visitados.add(estado_atual)
            vizinhos = gerar_vizinhos(no_atual, acaoCusto)
            nos_gerados += len(vizinhos)
            fila.extend(vizinhos)

    return {
        "estado_inicial": (x1, y1),
        "objetivo": (x2, y2),
        "caminho": None,
        "custo": math.inf,
        "nos_gerados": nos_gerados,
        "nos_visitados": len(visitados),
    }

# Outras implementações de algoritmos podem ser adicionadas aqui, como:
# busca_em_profundidade, busca_custo_uniforme, A*, etc.

def busca_em_profundidade(x1, y1, x2, y2, acaoCusto):
    pilha = [Node(x1, y1, 0, 0)]
    visitados = set()
    nos_gerados = 0

    while pilha:
        no_atual = pilha.pop()
        estado_atual = (no_atual.x, no_atual.y)

        if estado_atual == (x2, y2):
            return {
                "estado_inicial": (x1, y1),
                "objetivo": (x2, y2),
                "caminho": reconstruir_caminho(no_atual),
                "custo": no_atual.custo,
                "nos_gerados": nos_gerados,
                "nos_visitados": len(visitados),
            }

        if estado_atual not in visitados:
            visitados.add(estado_atual)
            vizinhos = gerar_vizinhos(no_atual, acaoCusto)
            nos_gerados += len(vizinhos)
            pilha.extend(vizinhos)

    return {
        "estado_inicial": (x1, y1),
        "objetivo": (x2, y2),
        "caminho": None,
        "custo": math.inf,
        "nos_gerados": nos_gerados,
        "nos_visitados": len(visitados),
    }

# Exemplos de funções de custo
def custo_c1(acao, _):
    return 10

def custo_c2(acao, _):
    return 10 if acao in {"f3", "f4"} else 15

def custo_c3(acao, t):
    return 10 if acao in {"f3", "f4"} else 10 + (abs(5 - t) % 6)

def custo_c4(acao, t):
    return 10 if acao in {"f3", "f4"} else 5 + (abs(10 - t) % 11)

# Execução de experimentos
def executar_experimento(algoritmo, x1, y1, x2, y2, acaoCusto):
    resultado = algoritmo(x1, y1, x2, y2, acaoCusto)
    print("Estado Inicial:", resultado["estado_inicial"])
    print("Objetivo:", resultado["objetivo"])
    print("Caminho Retornado:", resultado["caminho"])
    print("Custo do Caminho:", resultado["custo"])
    print("Nós Gerados:", resultado["nos_gerados"])
    print("Nós Visitados:", resultado["nos_visitados"])
    print()

# Testes
executar_experimento(busca_em_largura, 1, 3, 3, 3, custo_c1)
executar_experimento(busca_em_largura, 1, 3, 3, 3, custo_c2)
executar_experimento(busca_em_largura, 1, 3, 3, 3, custo_c3)
executar_experimento(busca_em_largura, 1, 3, 3, 3, custo_c4)

executar_experimento(busca_em_profundidade, 1, 3, 3, 3, custo_c1)
executar_experimento(busca_em_profundidade, 1, 3, 3, 3, custo_c2)
executar_experimento(busca_em_profundidade, 1, 3, 3, 3, custo_c3)
executar_experimento(busca_em_profundidade, 1, 3, 3, 3, custo_c4)