# C2. Ações na vertical (f3, f4) têm custo 10 e ações na horizontal (f1, f2) têm custo 15.
def custo_c2(node, t, acao):
    custo_incremental = 10 if acao in ['f3', 'f4'] else 15
    node.cost += custo_incremental
    return custo_incremental

