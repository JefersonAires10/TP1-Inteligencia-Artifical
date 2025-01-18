# main.py
import random
from collections import deque
import math

from algorithms.dfs import dfs
from algorithms.bfs import busca_em_largura


from actionCost.c1 import c1
from actionCost.c2 import c2
from actionCost.c3 import c3
from actionCost.c4 import c4


# experimento para o dfs
def experimento_dfs():
    x1, y1, x2, y2 = 0, 0, 9, 9
    acao_custo = c1  # Use c1, c2, c3 ou c4
    resultado = dfs(x1, y1, x2, y2, acao_custo)
    print(f"Resultado final: {resultado}")


if __name__ == "__main__":
    experimento_dfs()
