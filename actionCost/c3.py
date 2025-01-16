# C3. Ações na vertical (f3, f4) têm custo 10 e ações na horizontal (f1, f2) têm custo que
# varia com o tempo de trajeto segundo a função
# c3(t) = 10 + (|5 − t| mod 6),
def custo_c3(node, t, acao):
    custo_incremental = 10 if acao in ['f3', 'f4'] else 10 + (abs(5 - t) % 6)
    node.cost += custo_incremental
    return custo_incremental