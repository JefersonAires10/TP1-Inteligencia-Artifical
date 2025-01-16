from models.Busca import Busca
from models.Node import Estado

class BuscaEmProfundidade(Busca):
    def __init__(self, estado_inicial, objetivo, calcular_custo):
        super().__init__(estado_inicial, objetivo, calcular_custo)

    def buscar(self):
        pilha = [self.estado_inicial]

        while pilha:
            estado_atual = pilha.pop()
            profundidade = estado_atual.profundidade

            # Verificando se atingiu o objetivo
            if estado_atual == self.objetivo:
                return self.construir_saida(profundidade)

            # Ignora estados já visitados
            if estado_atual in self.visitados:
                continue

            self.visitados.add(estado_atual)

            # Função para calcular o custo
            def calcula_custo_acao(estado_atual, acao):
                custo = self.calcular_custo(estado_atual, acao)
                if custo is None:
                    print(f"Erro: Custo retornado como None para a ação {acao}")
                    return 0  # Retorna um valor padrão, como 0
                return custo

            # Criando os vizinhos
            vizinhos = [
                Estado(estado_atual.x - 1, estado_atual.y, profundidade + 1, estado_atual.cost + calcula_custo_acao(estado_atual, 'f1')),
                Estado(estado_atual.x + 1, estado_atual.y, profundidade + 1, estado_atual.cost + calcula_custo_acao(estado_atual, 'f2')),
                Estado(estado_atual.x, estado_atual.y - 1, profundidade + 1, estado_atual.cost + calcula_custo_acao(estado_atual, 'f3')),
                Estado(estado_atual.x, estado_atual.y + 1, profundidade + 1, estado_atual.cost + calcula_custo_acao(estado_atual, 'f4')),
            ]

            # Adicionando os vizinhos à pilha e atribuindo o caminho
            for vizinho in vizinhos:
                if vizinho not in self.visitados and vizinho.x >= 0 and vizinho.y >= 0:
                    self.nos_gerados += 1
                    pilha.append(vizinho)
                    self.caminho[vizinho] = estado_atual

        # Caso o objetivo não seja encontrado
        return self.construir_saida(None, erro=True)
