a = 1

def P():
    a = 3

def Q():
    a = 2
    P()
    print(a)

Q()

#print(a)