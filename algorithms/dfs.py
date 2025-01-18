from collections import deque
import math
from models.Node import Node, reconstruir_caminho

def dfs(x1, y1, x2, y2, acao_custo):
    no_inicial = Node(x1, y1, 0, 0, None, acao_custo)
    pilha = deque([no_inicial])
    nos_gerados = 1
    
    while pilha:
        no = pilha.pop()
        if no.x == x2 and no.y == y2:
            caminho = reconstruir_caminho(no)
            print(f"Caminho encontrado: {caminho}")
            return {
                "estado_inicial": (x1, y1),
                "objetivo": (x2, y2),
                "caminho": caminho,
                "custo": no.custo,
                "nos_gerados": nos_gerados,
                "nos_visitados": len(visitados_atual),
            }

        visitados_atual = set()
        visitados_atual.add((no.x, no.y))
        for vizinho in no.gerar_vizinhos(visitados_atual):
            pilha.append(vizinho)
            nos_gerados +=1
    return None