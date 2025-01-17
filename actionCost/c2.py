# C2. Ações na vertical (f3, f4) têm custo 10 e ações na horizontal (f1, f2) têm custo 15.
def custo_c2(acao, _):
    return 10 if acao in {"f3", "f4"} else 15
