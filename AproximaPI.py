#Autor: Alejandro Torices Oliva
#Muestra como utilizar pygame en programas

def aproximarPI(terminos):
    suma = 0    # ACUMULADOR
    for n in range(1, terminos+1):
        suma += (1/n**4)    # suma = suma + 1/n**2
    ap = (suma * 90)**0.25
    return ap


def main():
    terminos = int(input("Número de términos: "))
    valorPI = aproximarPI(terminos)
    print("PI =", valorPI)


main()
