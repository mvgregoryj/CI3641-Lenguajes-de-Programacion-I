def ins(e, ls):
    yield [e, *ls]
    if ls:
        for i in ins(e, ls[1:]):
            yield [ls[0], *i]

def misterio(ls):
    if ls:
        for m in misterio(ls[1:]):
            for i in ins(ls[0], m):
                yield i
    else:
        yield []

for m in misterio([1,2,3]):
    print (m)