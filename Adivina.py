import random


def generaNumero():
    numero = random.randint(1, 10)
    return numero


def main():
    intentos = 3
    z = 0
    aleatorio = generaNumero()
    print(aleatorio)
    while intentos !=0:
        guess = int(input("Ingresa tu respuesta: "))
        if guess != aleatorio:
            if guess > aleatorio:
                print("El número buscado es menor que tu respuesta.")
                intentos = intentos - 1
            else:
                print("El número buscado es mayor que tu respuesta.")
                intentos = intentos - 1
        else:
            print("Ganaste!!!")
            intentos = 0
            z = 3
    if intentos == 0 and z != 3:
        print("Perdiste :(")



main()