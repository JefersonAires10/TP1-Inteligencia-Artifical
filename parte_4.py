import random
import pandas as pd
from collections import deque
import math

# Importando as funções de busca
from algorithms.bfs import busca_em_largura
from algorithms.dfs import dfs

# Importando as funções de custo
from actionCost.c1 import c1
from actionCost.c2 import c2
from actionCost.c3 import c3
from actionCost.c4 import c4

# Definindo as funções de custo
custos = {
    "f1": c1,
    "f2": c2,
    "f3": c3,
    "f4": c4
}

# Configuração inicial
num_experimentos = 20
limite_coordenadas = 30
num_execucoes_por_par = 10
resultados = {
    "Busca em Largura": [],
    "Busca em Profundidade": []
}


# Laço de experimentação
for _ in range(num_experimentos):
    x1, y1 = random.randint(0, limite_coordenadas), random.randint(0, limite_coordenadas)
    x2, y2 = random.randint(0, limite_coordenadas), random.randint(0, limite_coordenadas)

    # Execuções para Busca em Largura
    for i in range(num_execucoes_por_par):
        for nome_custo, func_custo in custos.items():
            resultado = busca_em_largura(x1, y1, x2, y2, func_custo)
            resultados["Busca em Largura"].append({
                "Experimento": _,
                "Execução": i,
                "Estado Inicial": (x1, y1),
                "Objetivo": (x2, y2),
                "Caminho": resultado["caminho"] if resultado["caminho"] else "Erro",
                "Custo": resultado["custo"],
                "Nós Gerados": resultado["nos_gerados"],
                "Nós Visitados": resultado["nos_visitados"],
                "Função de Custo": nome_custo,
            })

    # Execuções para Busca em Profundidade
    for i in range(num_execucoes_por_par):
        for nome_custo, func_custo in custos.items():
            resultado = dfs(x1, y1, x2, y2, func_custo)
            resultados["Busca em Profundidade"].append({
                "Experimento": _,
                "Execução": i,
                "Estado Inicial": (x1, y1),
                "Objetivo": (x2, y2),
                 "Caminho": resultado["caminho"] if resultado["caminho"] else "Erro",
                "Custo": resultado["custo"],
                "Nós Gerados": resultado["nos_gerados"],
                "Nós Visitados": resultado["nos_visitados"],
                "Função de Custo": nome_custo,
            })


# Salvando em Excel
with pd.ExcelWriter("resultados_experimentacao_parte_4_final.xlsx") as writer:
    for nome_algoritmo, registros in resultados.items():
        df = pd.DataFrame(registros)
        df.to_excel(writer, sheet_name=nome_algoritmo, index=False)

print("Experimentação concluída e resultados salvos em 'resultados_experimentacao_parte_4_final.xlsx'")