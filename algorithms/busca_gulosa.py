from collections import deque
import math
from models.Node import Node, reconstruir_caminho
import heapq

def busca_gulosa(x1, y1, x2, y2, acao_custo, heuristica):
    heap = [Node(x1, y1, 0, 0, acao_custo=acao_custo)]  # Heap inicial com o nó raiz
    visitados = set()  # Para armazenar estados visitados
    nos_gerados = 0

    while heap:
        no_atual = heapq.heappop(heap)  # Remove o nó com menor custo (já atualizado com heuristica)
        estado_atual = (no_atual.x, no_atual.y)

        # Verifica se o objetivo foi alcançado
        if estado_atual == (x2, y2):
            return {
                "estado_inicial": (x1, y1),
                "objetivo": (x2, y2),
                "caminho": reconstruir_caminho(no_atual),
                "custo": no_atual.custo,
                "nos_gerados": nos_gerados,
                "nos_visitados": len(visitados),
            }

        # Adiciona o estado atual aos visitados se ainda não estiver lá
        if estado_atual not in visitados:
            visitados.add(estado_atual)

            # Gera os vizinhos que ainda não foram visitados
            vizinhos = no_atual.gerar_vizinhos(visitados)
            nos_gerados += len(vizinhos)

            # Adiciona os vizinhos ao heap, **filtrando os já visitados** e atualizando o custo com a heuristica
            for vizinho in vizinhos:
                if (vizinho.x, vizinho.y) not in visitados:
                    # Atualiza o custo do vizinho com a heuristica, mantendo o custo real do movimento (custo da ação)
                    vizinho.custo_total = heuristica(vizinho, Node(x2, y2, 0, 0))
                    heapq.heappush(heap, vizinho)

    # Caso não encontre o objetivo
    return {
        "estado_inicial": (x1, y1),
        "objetivo": (x2, y2),
        "caminho": None,
        "custo": math.inf,
        "nos_gerados": nos_gerados,
        "nos_visitados": len(visitados),
    }