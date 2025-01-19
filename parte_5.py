import pandas as pd

from actionCost.c1 import c1
from actionCost.c2 import c2
from actionCost.c3 import c3
from actionCost.c4 import c4
from algorithms.a_estrela_parada import gerar_coordenadas, a_estrela_parada
from heuristic.h1 import heuristica_h1
from heuristic.h2 import heuristica_h2


def executar_experimento_excel():
    limite = 30
    resultados = []

    for _ in range(25):  # 25 execuções
        # Gera coordenadas
        pontos = gerar_coordenadas(6, limite)
        (x1, y1), (x2, y2), *farmacias = pontos

        for func_custo in [c1, c2, c3, c4]:
            # Execução e armazenamento do A* com parada
            for heuristica in [heuristica_h1, heuristica_h2]:
                resultado = a_estrela_parada(
                    x1, y1, x2, y2, farmacias, func_custo, heuristica
                )
                if resultado:
                    resultados.append({
                        "Estado Inicial": (x1, y1),
                        "Objetivo": (x2, y2),
                        "Farmácias": farmacias,
                        "Função de Custo": func_custo.__name__,
                        "Heurística": heuristica.__name__,
                        "Caminho": resultado["caminho"],
                        "Custo Total": resultado["custo"],
                        "Nós Visitados": resultado["nos_visitados"],
                    })
                else:
                    resultados.append({
                        "Estado Inicial": (x1, y1),
                        "Objetivo": (x2, y2),
                        "Farmácias": farmacias,
                        "Função de Custo": func_custo.__name__,
                        "Heurística": heuristica.__name__,
                        "Caminho": "Nenhum",
                        "Custo Total": float("inf"),
                        "Nós Visitados": 0,
                    })

    # Cria um DataFrame pandas e salva como Excel
    df = pd.DataFrame(resultados)
    df.to_excel("resultados_experimentacao_parte_5.xlsx", index=False)

# Executa o experimento e salva no Excel
executar_experimento_excel()