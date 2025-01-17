from heapq import heappush, heappop
from models.Busca import Busca
from models.Node import Estado

class BuscaDeCustoUniforme(Busca):
    def __init__(self, estado_inicial, objetivo, calcular_custo):
        super().__init__(estado_inicial, objetivo, calcular_custo)

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

            # Criando os vizinhos
            acoes = ['f1', 'f2', 'f3', 'f4']
            for acao in acoes:
                if acao == 'f1':
                    novo_estado = Estado(estado_atual.x - 1, estado_atual.y, profundidade + 1)
                elif acao == 'f2':
                    novo_estado = Estado(estado_atual.x + 1, estado_atual.y, profundidade + 1)
                elif acao == 'f3':
                    novo_estado = Estado(estado_atual.x, estado_atual.y - 1, profundidade + 1)
                elif acao == 'f4':
                    novo_estado = Estado(estado_atual.x, estado_atual.y + 1, profundidade + 1)
                
                custo_incremental = self.calcular_custo(estado_atual, profundidade, acao)
                novo_estado.cost = estado_atual.cost + custo_incremental

                if novo_estado.x >= 0 and novo_estado.y >= 0:
                    self.nos_gerados += 1
                    if novo_estado not in custos or novo_estado.cost < custos[novo_estado]:
                        custos[novo_estado] = novo_estado.cost
                        heappush(fila, (novo_estado.cost, novo_estado))
                        self.caminho[novo_estado] = estado_atual

        return self.construir_saida(None, erro=True)