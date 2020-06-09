N2=2
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
n=N2    
while   n<1:
    n=collatzz(N2)
    print(n)
    
