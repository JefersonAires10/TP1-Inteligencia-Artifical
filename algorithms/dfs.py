from collections import deque
import math
from models.Node import Node, reconstruir_caminho

def dfs(x1, y1, x2, y2, acao_custo):
    visitados = set()
    no_inicial = Node(x1, y1, 0, 0, None, acao_custo)
    visitados.add((x1, y1))
    pilha = deque([no_inicial])
    nos_gerados = 1

    while pilha:
        no = pilha.pop()
        print(f"Nó atual: ({no.x}, {no.y}), Custo: {no.custo}, Profundidade: {no.profundidade}")
        if no.x == x2 and no.y == y2:
            caminho = reconstruir_caminho(no)
            print(f"Caminho encontrado: {caminho}")
            return {
                "estado_inicial": (x1, y1),
                "objetivo": (x2, y2),
                "caminho": caminho,
                "custo": no.custo,
                "nos_gerados": nos_gerados,
                "nos_visitados": len(visitados),
            }

        for vizinho in no.gerar_vizinhos(visitados):
            visitados.add((vizinho.x, vizinho.y))
            pilha.append(vizinho)
            nos_gerados +=1
    return None