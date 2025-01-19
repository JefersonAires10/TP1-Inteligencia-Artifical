from algorithms.dfs import dfs
from algorithms.bfs import busca_em_largura
from algorithms.aEstrela import a_estrela
from algorithms.busca_gulosa import busca_gulosa
from algorithms.dijkstra import dijkstra


from actionCost.c1 import c1
from actionCost.c2 import c2
from actionCost.c3 import c3
from actionCost.c4 import c4

from heuristic.h1 import heuristica_h1
from heuristic.h2 import heuristica_h2

# experimento para o dfs
def experimento_dfs():
    x1, y1, x2, y2 = 0, 0, 9, 9
    acao_custo = c1  # Use c1, c2, c3 ou c4
    resultado = dfs(x1, y1, x2, y2, acao_custo)
    print(f"Resultado final: {resultado}")

# experimento para o bfs
def experimento_bfs():
    x1, y1, x2, y2 = 0, 0, 9, 9
    acao_custo = c1  # Use c1, c2, c3 ou c4
    resultado = busca_em_largura(x1, y1, x2, y2, acao_custo)
    print(f"Resultado final: {resultado}")

# experimento para o aEstrela
def experimento_a_estrela():
    x1, y1, x2, y2 = 0, 0, 9, 9
    acao_custo = c1  # Use c1, c2, c3 ou c4
    heuristica = heuristica_h1  # Use heuristica_h1 ou heuristica_h2
    resultado = a_estrela(x1, y1, x2, y2, acao_custo, heuristica)
    print(f"Resultado final: {resultado}")

# experimento para o busca_gulosa
def experimento_busca_gulosa():
    x1, y1, x2, y2 = 0, 0, 9, 9
    acao_custo = c1  # Use c1, c2, c3 ou c4
    heuristica = heuristica_h1  # Use heuristica_h1 ou heuristica_h2
    resultado = busca_gulosa(x1, y1, x2, y2, acao_custo, heuristica)
    print(f"Resultado final: {resultado}")

# experimento para o dijkstra
def experimento_dijkstra():
    x1, y1, x2, y2 = 0, 0, 9, 9
    acao_custo = c1  # Use c1, c2, c3 ou c4
    resultado = dijkstra(x1, y1, x2, y2, acao_custo)
    print(f"Resultado final: {resultado}")


if __name__ == "__main__":
    # experimento_dfs()
    # experimento_bfs()
    # experimento_a_estrela()
    # experimento_busca_gulosa()
    experimento_dijkstra()
