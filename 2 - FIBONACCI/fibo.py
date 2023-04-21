
def fibo(numero):
    futuro = 0
    presente = 0
    passado = 0
    fiboList = []
    for x in range(numero):
        if(x==0):
            passado += 0
        if(x==1):
            presente += 1
        futuro = presente+passado
        presente = passado
        passado = futuro
        #presente = passado
        #print("presente{} \n passado{} \n futuro{}".format(presente,passado,futuro))
        fiboList.append(futuro)
    return fiboList
def retTrue(list,escolha):
    if(escolha in list):return True
    else:return False
        

if __name__ == '__main__':
    NumeroLimite = int(input("Fibonacci Limite:"))
    listFibo = fibo(NumeroLimite)
    

    
    Escolha = int(input("Digite o Numero A ser Verificado"))
    if(retTrue(listFibo,Escolha)==True):
        print("Numero na Seguencia Fibonacci")
    else:
        print("Numero Não esta na Seguencia")
    
    print(" LISTA CRIADA: {0}".format(listFibo))