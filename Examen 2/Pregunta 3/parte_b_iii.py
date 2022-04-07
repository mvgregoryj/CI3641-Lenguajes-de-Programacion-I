# --------------------------------------------------
# Suspenso 1: 
# Modificando el iterador misterio que usa el iterador ins.

def ins(e, ls):
    yield [e, *ls]
    if ls:
        for i in ins(e, ls[1:]):
            yield [ls[0], *i]

def suspenso(ls):
    if len(ls) > 1:
        arreglo = []
        for m in suspenso(ls[1:]):
            arreglo.append(m)
            if len(arreglo) == len(ls)-1:
                for i in ins(ls[0], arreglo):
                    for j in i:
                        yield j
                arreglo = []
    else:
        yield ls[0]


# --------------------------------------------------
# Suspenso 2:
# Creando un iterador suspenso2 que usa el iterador misterio y el iterador ins

def misterio(ls):
    if ls:
        for m in misterio(ls[1:]):
            for i in ins(ls[0], m):
                yield i
    else:
        yield []

def suspenso2(ls):
    if ls:
        for m in misterio(ls):
            for i in m:
                yield i
    else:
        yield []

if __name__ == "__main__":
    print("Suspenso:")
    for k in suspenso([1,2,3]):
        print(k)

    print("\n\nSuspenso 2:")
    for s in suspenso2([1,2,3]):
        print (s)