# C1. Todas as ações (f1, f2, f3, f4) têm custo 10, independente da direção.
def custo_c1(node, t, acao):
    custo_incremental = 10
    node.cost += custo_incremental
    return custo_incremental