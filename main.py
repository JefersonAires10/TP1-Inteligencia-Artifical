import random
import math
from algorithms.aEstrela import a_estrela
from algorithms.dijkstra import dijkstra
# from actionCost import c1 as c1, c2 as c2, c3 as c3, c4 as c4

from heuristic.h1 import heuristica_h1
from heuristic.h2 import heuristica_h2


def executar_experimentos(num_execucoes=50):
    def c1(acao, _):
        return 10

    def c2(acao, _):
        return 10 if acao in {"f3", "f4"} else 15

    def c3(acao, t):
        return 10 if acao in {"f3", "f4"} else 10 + (abs(5 - t) % 6)

    def c4(acao, t):
        return 10 if acao in {"f3", "f4"} else 5 + (abs(10 - t) % 11)

    resultados = []
    funcoes_custo = [c1, c2, c3, c4]
    funcoes_heuristicas = [heuristica_h1, heuristica_h2]
    
    for _ in range(num_execucoes):
        # Gera coordenadas aleatórias
        x1 = random.randint(0, 9)
        y1 = random.randint(0, 9)
        x2 = random.randint(0, 9)
        y2 = random.randint(0, 9)
        
        # Executa Busca de Custo Uniforme
        for acao_custo in funcoes_custo:
             resultado = dijkstra(x1, y1, x2, y2, acao_custo)
             resultados.append({
                 "algoritmo": "Custo Uniforme",
                 "funcao_custo": acao_custo.__name__,
                 "estado_inicial": (x1, y1),
                 "objetivo": (x2, y2),
                 "caminho": resultado["caminho"],
                 "custo": resultado["custo"],
                 "nos_gerados": resultado["nos_gerados"],
                 "nos_visitados": resultado["nos_visitados"],
             })
        
        # Executa Busca A*
        for acao_custo in funcoes_custo:
            for heuristica in funcoes_heuristicas:
                resultado = a_estrela(x1, y1, x2, y2, acao_custo, heuristica)
                resultados.append({
                    "algoritmo": "A*",
                    "funcao_custo": acao_custo.__name__,
                    "heuristica": heuristica.__name__,
                    "estado_inicial": (x1, y1),
                    "objetivo": (x2, y2),
                    "caminho": resultado["caminho"],
                    "custo": resultado["custo"],
                    "nos_gerados": resultado["nos_gerados"],
                    "nos_visitados": resultado["nos_visitados"],
                })
    return resultados


def salvar_resultados(resultados, nome_arquivo="resultados_experimento.txt"):
    with open(nome_arquivo, "w") as arquivo:
        for resultado in resultados:
            linha = ", ".join(f"{chave}: {valor}" for chave, valor in resultado.items())
            arquivo.write(linha + "\n")
    print(f"Resultados salvos em {nome_arquivo}")


if __name__ == "__main__":
    resultados = executar_experimentos()
    salvar_resultados(resultados)