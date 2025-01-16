def heuristica_h2(atual, objetivo):
    # Distância Euclidiana
    return ((atual.x - objetivo.x) ** 2 + (atual.y - objetivo.y) ** 2) ** 0.5