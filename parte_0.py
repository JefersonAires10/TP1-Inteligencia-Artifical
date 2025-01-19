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
resultados = {}


# Função para executar um algoritmo específico
def executar_algoritmo(algoritmo, x1, y1, x2, y2, func_custo=None, func_heuristica=None):
    if algoritmo == "Dijkstra":
        return dijkstra(x1, y1, x2, y2, func_custo)
    elif algoritmo == "A*":
        return a_estrela(x1, y1, x2, y2, func_custo, func_heuristica)
    elif algoritmo == "BFS":
        return busca_em_largura(x1, y1, x2, y2, func_custo)
    elif algoritmo == "DFS":
        return dfs(x1, y1, x2, y2, func_custo)
    elif algoritmo == "Busca Gulosa":
        return busca_gulosa(x1, y1, x2, y2, func_custo, func_heuristica)
    else:
        return None


# Laço de experimentação
for _ in range(num_experimentos):
    x1, y1 = random.randint(0, limite_coordenadas), random.randint(0, limite_coordenadas)
    x2, y2 = random.randint(0, limite_coordenadas), random.randint(0, limite_coordenadas)

    for nome_algoritmo in ["Dijkstra", "A*", "BFS", "DFS", "Busca Gulosa"]:
        # Inicializa a lista de resultados para o algoritmo, se necessário
        if nome_algoritmo not in resultados:
            resultados[nome_algoritmo] = []

        # Execução para cada combinação de custo e heurística
        for nome_custo, func_custo in custos.items():
             if nome_algoritmo in ["A*", "Busca Gulosa"]:
                for nome_heuristica, func_heuristica in heuristicas.items():
                    resultado = executar_algoritmo(nome_algoritmo, x1, y1, x2, y2, func_custo, func_heuristica)
                    resultados[nome_algoritmo].append({
                        "Estado Inicial": (x1, y1),
                        "Objetivo": (x2, y2),
                        "Caminho": resultado["caminho"] if resultado and resultado["caminho"] else "Erro",
                        "Custo": resultado["custo"] if resultado else None,
                        "Nós Gerados": resultado["nos_gerados"] if resultado else None,
                        "Nós Visitados": resultado["nos_visitados"] if resultado else None,
                        "Função de Custo": nome_custo,
                        "Heurística": nome_heuristica,
                    })

             else:
                    resultado = executar_algoritmo(nome_algoritmo, x1, y1, x2, y2, func_custo=func_custo)

                    resultados[nome_algoritmo].append({
                        "Estado Inicial": (x1, y1),
                        "Objetivo": (x2, y2),
                        "Caminho": resultado["caminho"] if resultado and resultado["caminho"] else "Erro",
                        "Custo": resultado["custo"] if resultado else None,
                        "Nós Gerados": resultado["nos_gerados"] if resultado else None,
                        "Nós Visitados": resultado["nos_visitados"] if resultado else None,
                        "Função de Custo": nome_custo,
                    })

# Salvando em Excel
with pd.ExcelWriter("resultados_experimentacao_parte_0.xlsx") as writer:
    for nome_algoritmo, registros in resultados.items():
        df = pd.DataFrame(registros)
        sheet_name = nome_algoritmo.replace("*", "estrela")  # Substituir '*'
        df.to_excel(writer, sheet_name=sheet_name, index=False)

print("Experimentação concluída e resultados salvos em 'resultados_experimentacao_parte_0.xlsx'")