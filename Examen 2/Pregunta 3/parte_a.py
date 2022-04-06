def ins(e, ls):
    yield [e, *ls]
    if ls:
        for i in ins(e, ls[1:]):
            yield [ls[0], *i]

for i in ins(0, [1, 2, 3]):
    print (i)