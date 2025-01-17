import heapq
from models.Node import Node, reconstruir_caminho

def a_estrela(x1, y1, x2, y2, acao_custo, heuristica):
    # Inicializa o heap com o nó raiz, incluindo o custo heurístico
    heap = [Node(x1, y1, 0, 0, acao_custo=acao_custo)]
    visitados = set()
    nos_gerados = 0

    while heap:
        no_atual = heapq.heappop(heap)
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

            for vizinho in vizinhos:
                if (vizinho.x, vizinho.y) not in visitados:
                    # Adiciona o custo heurístico ao custo do vizinho
                    vizinho.custo += heuristica(vizinho, Node(x2, y2, 0, 0))
                    heapq.heappush(heap, vizinho)

    return {
        "estado_inicial": (x1, y1),
        "objetivo": (x2, y2),
        "caminho": None,
        "custo": float("inf"),
        "nos_gerados": nos_gerados,
        "nos_visitados": len(visitados),
    }