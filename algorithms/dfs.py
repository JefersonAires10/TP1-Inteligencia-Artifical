from models.Busca import Busca
from models.Node import Estado

class BuscaEmProfundidade(Busca):
    def __init__(self, estado_inicial, objetivo, calcular_custo):
        super().__init__(estado_inicial, objetivo, calcular_custo)
        self.limite_profundidade = 10  # Defina um limite de profundidade para evitar loops infinitos

    def buscar(self):
        pilha = [(self.estado_inicial, 0)]  # Usamos tuplas (estado, tempo)

        while pilha:
            estado_atual, tempo = pilha.pop()
            profundidade = estado_atual.profundidade

            # Verificando se atingiu o objetivo
            if estado_atual == self.objetivo:
                return self.construir_saida(profundidade)

            # Ignora estados já visitados
            if estado_atual in self.visitados:
                continue

            self.visitados.add(estado_atual)

            # Limite de profundidade atingido
            if profundidade >= self.limite_profundidade:
                continue

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
                
                custo_incremental = self.calcular_custo(estado_atual, tempo, acao)
                novo_estado.cost = estado_atual.cost + custo_incremental
                
                # Adicionando o vizinho à pilha e atribuindo o caminho
                if novo_estado.x >= 0 and novo_estado.y >= 0:
                    self.nos_gerados += 1
                    pilha.append((novo_estado, tempo+1))
                    
                    # Verifica se o estado já está no caminho ou se o novo custo é menor
                    if novo_estado not in self.caminho or (self.caminho[novo_estado] is not None and novo_estado.cost < self.caminho[novo_estado].cost):
                        self.caminho[novo_estado] = estado_atual
        # Caso o objetivo não seja encontrado
        return self.construir_saida(None, erro=True)