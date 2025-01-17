from collections import deque
from models.Busca import Busca
from models.Node import Estado
class BuscaEmLargura(Busca):
    def __init__(self, estado_inicial, objetivo, calcular_custo):
        super().__init__(estado_inicial, objetivo, calcular_custo)

    def buscar(self):
        fila = deque([self.estado_inicial])

        while fila:
            estado_atual = fila.popleft()
            profundidade = estado_atual.profundidade
            if estado_atual == self.objetivo:
                return self.construir_saida(profundidade)

            if estado_atual in self.visitados:
                continue

            self.visitados.add(estado_atual)

            # Verificando se o custo calculado é válido
            def calcula_custo_acao(estado_atual, profundidade, acao):
                custo = self.calcular_custo(estado_atual, profundidade, acao)
                if custo is None:
                    # Se retornar None, substitua por um valor padrão (ex: 0)
                    print(f"Erro: Custo retornado como None para a ação {acao}")
                    return 0  # ou algum outro valor adequado
                return custo

            vizinhos = [
                Estado(estado_atual.x - 1, estado_atual.y, profundidade + 1, estado_atual.cost + calcula_custo_acao(estado_atual, profundidade, 'f1')),
                Estado(estado_atual.x + 1, estado_atual.y, profundidade + 1, estado_atual.cost + calcula_custo_acao(estado_atual, profundidade, 'f2')),
                Estado(estado_atual.x, estado_atual.y - 1, profundidade + 1, estado_atual.cost + calcula_custo_acao(estado_atual, profundidade, 'f3')),
                Estado(estado_atual.x, estado_atual.y + 1, profundidade + 1, estado_atual.cost + calcula_custo_acao(estado_atual, profundidade, 'f4')),
            ]

            for vizinho in vizinhos:
                if vizinho not in self.visitados and vizinho.x >= 0 and vizinho.y >= 0:
                    self.nos_gerados += 1
                    fila.append(vizinho)
                    self.caminho[vizinho] = estado_atual

        return self.construir_saida(None, erro=True)
