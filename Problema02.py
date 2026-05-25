def suma_recursiva(lista, pi, pf):
    if pi > pf:
        return 0
    return lista[pi - 1] + suma_recursiva(lista, pi + 1, pf)

lista = [2, 4, 6, 3]
pi = 2
pf = 3
print(f"lista: {lista}, PI={pi}, PF={pf}")
print(f"resultado: {suma_recursiva(lista, pi, pf)}")