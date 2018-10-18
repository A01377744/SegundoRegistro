# Alejandro Torices Oliva
# Es un número que recibe un número y lo regresa invertido

def invertirNúmero(x):
    z = 0
    while x != 0:
        y = x % 10
        x = x//10
        z = z*10 + y
    return z



def main():
    numero = int(input("número="))
    invertido = invertirNúmero(numero)
    print(invertido)

main()

