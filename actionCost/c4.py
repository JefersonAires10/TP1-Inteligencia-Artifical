# Ações na vertical (f3, f4) têm custo 10 e ações na horizontal (f1, f2) têm custo que
# varia com o tempo de trajeto segundo a função
# c4(t) = 5 + (|10 − t| mod 11)
def custo_c4(acao, t):
    return 10 if acao in {"f3", "f4"} else 5 + (abs(10 - t) % 11)
