class Busca:
    def __init__(self, estado_inicial, objetivo, calcular_custo, heuristica=None):
        self.estado_inicial = estado_inicial
        self.objetivo = objetivo
        self.calcular_custo = calcular_custo
        self.heuristica = heuristica
        self.nos_gerados = 0
        self.visitados = set()
        self.caminho = {estado_inicial: None}

    def construir_saida(self, profundidade, erro=False):
        if erro:
            return {
                "Estado Inicial": self.estado_inicial,
                "Objetivo": self.objetivo,
                "Caminho": "Erro: Caminho não encontrado",
                "Custo Total": "∞",
                "Nós Gerados": self.nos_gerados,
                "Nós Visitados": len(self.visitados),
            }

        estado = self.objetivo
        caminho_reconstituido = []
        custo_total = 0
        while estado:
            caminho_reconstituido.append(estado)
            custo_total = estado.cost  # Atualiza o custo total com o custo do estado atual
            estado = self.caminho[estado]

        caminho_reconstituido.reverse()

        return {
            "Estado Inicial": self.estado_inicial,
            "Objetivo": self.objetivo,
            "Caminho": caminho_reconstituido,
            "Custo Total": custo_total,
            "Nós Gerados": self.nos_gerados,
            "Nós Visitados": len(self.visitados),
        }