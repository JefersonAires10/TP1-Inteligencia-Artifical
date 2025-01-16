# Funções heurísticas
def heuristica_h1(atual, objetivo):
    # Distância de Manhattan
    return abs(atual.x - objetivo.x) + abs(atual.y - objetivo.y)