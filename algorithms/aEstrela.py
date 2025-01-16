from heapq import heappush, heappop
from models.Busca import Busca
from models.Node import Estado

class BuscaAEstrela(Busca):
    def buscar(self):
        fila = [(0, self.estado_inicial, 0)]
        while fila:
            _, estado_atual, profundidade = heappop(fila)
            if estado_atual == self.objetivo:
                return self.construir_saida(profundidade)

            if estado_atual in self.visitados:
                continue

            self.visitados.add(estado_atual)

            # Gerar vizinhos
            vizinhos = [
                (Estado(estado_atual.x - 1, estado_atual.y, profundidade + 1), 'f1'),
                (Estado(estado_atual.x + 1, estado_atual.y, profundidade + 1), 'f2'),
                (Estado(estado_atual.x, estado_atual.y - 1, profundidade + 1), 'f3'),
                (Estado(estado_atual.x, estado_atual.y + 1, profundidade + 1), 'f4'),
            ]

            for vizinho, acao in vizinhos:
                if vizinho not in self.visitados and vizinho.x >= 0 and vizinho.y >= 0:
                    self.nos_gerados += 1
                    custo = self.calcular_custo(acao, profundidade) + self.heuristica(vizinho, self.objetivo)
                    heappush(fila, (custo, vizinho, profundidade + 1))
                    self.caminho[vizinho] = estado_atual

        return self.construir_saida(None, erro=True)
        