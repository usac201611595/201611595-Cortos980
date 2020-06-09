N2=3
def EsPar(N):      
        if N % 2 == 0:
            return True
        else:
            return False


def collatzz(Numero):
    if Numero>1:
        if EsPar(Numero):
            Numero=int(Numero/2)
        else:
            Numero=[3*Numero+1]
    else:
        Numero=1
    return Numero
    
n=collatzz(N2)
print(n)
if n<1:
    n=collatzz(n)
    print(n)
    
