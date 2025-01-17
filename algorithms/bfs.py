from collections import deque
import math
from models.Node import Node, reconstruir_caminho

def busca_em_largura(x1, y1, x2, y2, acao_custo):
    fila = deque([Node(x1, y1, 0, 0, acao_custo = acao_custo)])
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
            vizinhos = no_atual.gerar_vizinhos(visitados)
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