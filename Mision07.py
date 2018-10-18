# Autor: Alejandro Torices Oliva
# Es un programa que despliega un menu y permite elegir entre calcular divisiones y encontrar el número mayor.


# Es una función que recibe los datos de una división, la calcula y la imprime.
def dividir(dividendo, divisor):
    cociente = 0
    if divisor == 0:
        print('math error')
        print('')
    elif dividendo <= 0 or divisor <= 0:
        print('Ingrese solamente números positivos')
        print('')
    else:
        dividendoOriginal = dividendo
        while dividendo >= divisor:
            dividendo = dividendo - divisor
            cociente = cociente + 1
        print('%d / %d = %d, sobra %d' % (dividendoOriginal, divisor, cociente, dividendo))
        print('')


# Es una función que recibe valores hasta que se introduce el -1 y regresa el mayor número introducido.
def encontrarMayor():
    numeroMayor = 0
    numero = 0
    while numero != -1:
        numero = int(input('Teclea un número [-1 para salir]: '))
        if numero > numeroMayor:
            numeroMayor = numero
        elif numero < numeroMayor:
            numeroMayor = numeroMayor
    if numeroMayor > 0:
        print('El mayor es:', numeroMayor)
        print('')
    if numero == -1 and numeroMayor == 0:
        print('No hay número mayor')
        print('')


# Es la función principal
def main():
    opcion = 0
    while opcion != 3:
        print('''Mision 07. Ciclos while
Autor: Alejandro Torices Oliva
Matrícula: A01377744
1. Calcular divisiones
2. Encontrar el mayor
3. Salir''')
        opcion = int(input('Teclea tu opción: '))
        print('')
        if opcion == 1:
            print('Calculando divisiones')
            print('Ingrese solamente números positivos')
            dividendo = int(input('Dividendo: '))
            divisor = int(input('Divisor: '))
            dividir(dividendo, divisor)

        elif opcion == 2:
            encontrarMayor()
        elif opcion == 3:
            print('')
            print('Gracias por usar este programa, regresa pronto.')
        else:
            print('ERROR, Teclea 1, 2 o 3')
            print('')


main()
