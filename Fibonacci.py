def problema1():
    lista = []
    for x in range(3, 1000):
        if x % 3 == 0 or x % 5 == 0:
            lista.append(x)
    print(sum(lista))

def crearSecuenciaFibonacci(terminos):
    fibonacci = [1, 1, 2]
    for x in range(0, terminos):
        numero = fibonacci[1+x] + fibonacci[2+x]
        fibonacci.append(numero)
    return fibonacci


def problema2():
    terminos = int(input('Ingrese los números que desee conocer:'))
    fibonacci = crearSecuenciaFibonacci(terminos)
    newFibonacci = []
    for x in fibonacci:
        if x <= 4000000 and x % 2 == 0:
            newFibonacci.append(x)
    suma = sum(newFibonacci)
    print(suma)


def problema5():
    newLista = []
    listas = list(range(10000000, 100000000))
    for x in listas:
        if x % 11 == 0 and x % 12 == 0 and x % 13 == 0 and x % 14 == 0 and x % 15 == 0 and x % 16 == 0 and x % 17 == 0 and x % 18 == 0 and x % 19 == 0 and x % 20 == 0:
            newLista.append(x)
    print(newLista)
problema5()
