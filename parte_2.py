import random
import pandas as pd

from algorithms.dijkstra import dijkstra
from algorithms.aEstrela import a_estrela
from algorithms.bfs import busca_em_largura
from algorithms.dfs import dfs
from algorithms.busca_gulosa import busca_gulosa

from actionCost.c1 import c1
from actionCost.c2 import c2
from actionCost.c3 import c3
from actionCost.c4 import c4

from heuristic.h1 import heuristica_h1
from heuristic.h2 import heuristica_h2

# Funções de custo já definidas
custos = {
    "f1": c1,
    "f2": c2,
    "f3": c3,
    "f4": c4
}

# Funções heurísticas já definidas
heuristicas = {
    "h1": heuristica_h1,
    "h2": heuristica_h2
}

# Configuração inicial
num_experimentos = 50
limite_coordenadas = 10  # Coordenadas aleatórias entre 0 e limite_coordenadas
resultados = {
    "Custo_Uniforme": [],
    "A*": []
}

# Laço de experimentação
for _ in range(num_experimentos):
    x1, y1 = random.randint(0, limite_coordenadas), random.randint(0, limite_coordenadas)
    x2, y2 = random.randint(0, limite_coordenadas), random.randint(0, limite_coordenadas)

    # Execução e armazenamento da busca de custo uniforme
    for nome_custo, func_custo in custos.items():
        resultado = dijkstra(x1, y1, x2, y2, func_custo)

        # Armazenando resultados
        resultados["Custo_Uniforme"].append({
            "Estado Inicial": (x1, y1),
            "Objetivo": (x2, y2),
            "Caminho": resultado["caminho"] if resultado["caminho"] else "Erro",
            "Custo": resultado["custo"],
            "Nós Gerados": resultado["nos_gerados"],
            "Nós Visitados": resultado["nos_visitados"],
            "Função de Custo": nome_custo,
        })

    # Execução e armazenamento do A*
    for nome_custo, func_custo in custos.items():
        for nome_heuristica, func_heuristica in heuristicas.items():
            resultado = a_estrela(x1, y1, x2, y2, func_custo, func_heuristica)

            # Armazenando resultados
            resultados["A*"].append({
                "Estado Inicial": (x1, y1),
                "Objetivo": (x2, y2),
                "Caminho": resultado["caminho"] if resultado["caminho"] else "Erro",
                "Custo": resultado["custo"],
                "Nós Gerados": resultado["nos_gerados"],
                "Nós Visitados": resultado["nos_visitados"],
                "Função de Custo": nome_custo,
                "Heurística": nome_heuristica
            })


# Salvando em Excel
with pd.ExcelWriter("experimentacoes/resultados_experimentacao_parte_2.xlsx") as writer:
    for nome_algoritmo, registros in resultados.items():
        df = pd.DataFrame(registros)
        sheet_name = nome_algoritmo.replace("*", "estrela")  # Substituir '*'
        df.to_excel(writer, sheet_name=sheet_name, index=False)

print("Experimentação concluída e resultados salvos em 'resultados_experimentacao_parte_2.xlsx'")