from models.Node import Estado
from algorithms.bfs import BuscaEmLargura
from algorithms.dfs import BuscaEmProfundidade
from actionCost.c1 import custo_c1
from actionCost.c2 import custo_c2
from actionCost.c3 import custo_c3
from actionCost.c4 import custo_c4

if __name__ == "__main__":
    estado_inicial = Estado(0, 0)
    objetivo = Estado(2, 2)

    cenarios = {
        "C1": custo_c1,
        "C2": custo_c2,
        "C3": custo_c3,
        "C4": custo_c4,
    }

    # Configurar experimento
    calcular_custo = cenarios["C1"] 
    # algoritmo = BuscaEmLargura(estado_inicial, objetivo, calcular_custo)
    algoritmo = BuscaEmProfundidade(estado_inicial, objetivo, calcular_custo)

    resultado = algoritmo.buscar()
    for chave, valor in resultado.items():
        print(f"{chave}: {valor}")