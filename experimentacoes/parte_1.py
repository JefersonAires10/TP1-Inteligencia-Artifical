import random
import pandas as pd

from algorithms.dfs import dfs
from algorithms.bfs import busca_em_largura
from algorithms.dijkstra import dijkstra

from actionCost.c1 import c1
from actionCost.c2 import c2
from actionCost.c3 import c3
from actionCost.c4 import c4

custos = {
    "f1": c1,
    "f2": c2,
    "f3": c3,
    "f4": c4
}

# Configuração inicial
num_experimentos = 50
limite_coordenadas = 10
resultados = {
    "BFS": [],
    "DFS": [],
    "Custo_Uniforme": []
}

# Laço de experimentação
for _ in range(num_experimentos):
    # Gera coordenadas aleatórias para o estado inicial e objetivo
    x1, y1 = random.randint(0, limite_coordenadas), random.randint(0, limite_coordenadas)
    x2, y2 = random.randint(0, limite_coordenadas), random.randint(0, limite_coordenadas)

    # Execução e armazenamento da busca em largura, busca em profundidade e busca de custo uniforme
    for nome_algoritmo, algoritmo in zip(["BFS", "DFS", "Custo_Uniforme"], [busca_em_largura, dfs, dijkstra]):
        for nome_custo, func_custo in custos.items():
            resultado = algoritmo(x1, y1, x2, y2, func_custo)

            # Armazenando resultados
            resultados[nome_algoritmo].append({
                "Estado Inicial": (x1, y1),
                "Objetivo": (x2, y2),
                "Caminho": resultado["caminho"] if resultado["caminho"] else "Erro",
                "Custo": resultado["custo"],
                "Nós Gerados": resultado["nos_gerados"],
                "Nós Visitados": resultado["nos_visitados"],
                "Função de Custo": nome_custo
            })

# Salvando em Excel
with pd.ExcelWriter("resultados_experimentacao_parte_1.xlsx") as writer:
    for nome_algoritmo, registros in resultados.items():
        df = pd.DataFrame(registros)
        df.to_excel(writer, sheet_name=nome_algoritmo, index=False)

print("Experimentação concluída e resultados salvos em 'resultados_experimentacao.xlsx'")
