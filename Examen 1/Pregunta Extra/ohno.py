import math

def trib(n):
    if 0<=n<3:
        return n
    elif n >= 3:
        return trib(n-1) + trib(n-2) + trib(n-3)

def catalan(n: int):
	res=0
	if n==0:
		res=1
	elif n!=0:
		res=(2*(2*n-1)*catalan(n-1))//(n+1)
	return res

def logBase2(n):
    return math.log(n, 2)

def ohno(n):
    return math.floor(logBase2(catalan(trib(catalan(n)+1))))

while True:
    n = int(input("Valor mayor o igual a 0: "))
    if n >= 0:
            print(f"onho{n} = {ohno(n)}")
    else:
        print(f"No ingreso un valor de n >= 0")