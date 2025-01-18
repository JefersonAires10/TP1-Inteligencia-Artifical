from collections import deque
import math
from models.Node import Node, reconstruir_caminho


def dfs(x1, y1, x2, y2, acao_custo):
    nos_gerados = 0
    nos_visitados = 0
    inicio = Node(x1, y1, 0, 0, acao_custo=acao_custo)
    objetivo = Node(x2, y2, 0, 0, acao_custo=acao_custo)
    fronteira = [inicio]
    visitados = set()

    while fronteira:
        no = fronteira.pop()
        nos_visitados += 1
        visitados.add((no.x, no.y))

        if (no.x, no.y) == (objetivo.x, objetivo.y):
            caminho = reconstruir_caminho(no)
            custo_total = no.custo
            return {
                "estado_inicial": (x1, y1),
                "objetivo_busca": (x2, y2),
                "caminho": caminho,
                "custo": custo_total,
                "nos_gerados": nos_gerados,
                "nos_visitados": nos_visitados
            }

        vizinhos = no.gerar_vizinhos(visitados)
        nos_gerados += len(vizinhos)

        for vizinho in vizinhos:
            fronteira.append(vizinho)

    return {
        "estado_inicial": (x1, y1),
        "objetivo_busca": (x2, y2),
        "caminho": "Erro - Caminho Não Encontrado",
        "custo": float('inf'),
        "nos_gerados": nos_gerados,
        "nos_visitados": nos_visitados,
    }