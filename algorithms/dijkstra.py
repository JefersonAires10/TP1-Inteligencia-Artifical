from models.Busca import Busca
from models.Node import Estado
from heapq import heappush, heappop

class BuscaDeCustoUniforme(Busca):
    def buscar(self):
        fila = []
        heappush(fila, (0, self.estado_inicial))
        custos = {self.estado_inicial: 0}

        while fila:
            _, estado_atual = heappop(fila)
            profundidade = estado_atual.profundidade

            if estado_atual == self.objetivo:
                return self.construir_saida(profundidade)

            if estado_atual in self.visitados:
                continue

            self.visitados.add(estado_atual)

            vizinhos = [
                Estado(estado_atual.x - 1, estado_atual.y, profundidade + 1, estado_atual.cost + self.calcular_custo('f1', profundidade)),
                Estado(estado_atual.x + 1, estado_atual.y, profundidade + 1, estado_atual.cost + self.calcular_custo('f2', profundidade)),
                Estado(estado_atual.x, estado_atual.y - 1, profundidade + 1, estado_atual.cost + self.calcular_custo('f3', profundidade)),
                Estado(estado_atual.x, estado_atual.y + 1, profundidade + 1, estado_atual.cost + self.calcular_custo('f4', profundidade)),
            ]

            for vizinho in vizinhos:
                if vizinho.x >= 0 and vizinho.y >= 0:
                    self.nos_gerados += 1
                    if vizinho not in custos or vizinho.cost < custos[vizinho]:
                        custos[vizinho] = vizinho.cost
                        heappush(fila, (vizinho.cost, vizinho))
                        self.caminho[vizinho] = estado_atual

        return self.construir_saida(None, erro=True)
