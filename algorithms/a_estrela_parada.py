import heapq
import random

from models.Node import Node, reconstruir_caminho


# Função para gerar coordenadas aleatórias únicas
def gerar_coordenadas(quantidade, limite):
    coordenadas = set()
    while len(coordenadas) < quantidade:
        coordenadas.add((random.randint(0, limite), random.randint(0, limite)))
    return list(coordenadas)

# Modificação da Busca A*
def a_estrela_parada(x1, y1, x2, y2, farmacias, acao_custo, heuristica):
    # Inicializa o heap com o nó raiz
    inicial = Node(x1, y1, 0, 0, acao_custo=acao_custo)
    heap = [inicial]
    visitados = set()
    passou_por_farmacia = False

    while heap:
        no_atual = heapq.heappop(heap)
        estado_atual = (no_atual.x, no_atual.y)

        # Verifica se o nó é uma farmácia
        if estado_atual in farmacias:
            passou_por_farmacia = True

        # Verifica se atingiu o destino e passou por uma farmácia
        if estado_atual == (x2, y2) and passou_por_farmacia:
            return {
                "estado_inicial": (x1, y1),
                "objetivo": (x2, y2),
                "caminho": reconstruir_caminho(no_atual),
                "custo": no_atual.custo,
                "nos_visitados": len(visitados),
            }

        # Adiciona o estado atual aos visitados se ainda não estiver lá
        if estado_atual not in visitados:
            visitados.add(estado_atual)
            vizinhos = no_atual.gerar_vizinhos(visitados)

            # Adiciona os vizinhos ao heap, **filtrando os já visitados** e atualizando o custo com a heuristica
            for vizinho in vizinhos:
                if (vizinho.x, vizinho.y) not in visitados:
                    # Adiciona o custo heurístico
                    vizinho.custo += heuristica(vizinho, Node(x2, y2, 0, 0))
                    heapq.heappush(heap, vizinho)

    return None  # Não encontrou solução