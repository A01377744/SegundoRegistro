'''colores = ["rojo", "azul", "amarillo", "verde", "morado", "naranja"]
ornitorrinco = list('ornitorrinco')
print(ornitorrinco)
print(colores)
list.append(ornitorrinco, 's')
print(ornitorrinco)'''


def hacerListas():
    lista = []
    numeros = 0
    while numeros != -1:                # Hace la lista y corta el proceso cuando se introduce -1
        numeros = int(input("Números de la lista: "))
        if numeros == -1:
            break
        list.append(lista, numeros)

    promedio = sum(lista) / len(lista)  # Calcula el promedio

    b = list.copy(lista)                # Copia la lista y la modifica
    list.append(b, 'bbbbbb')

    newList = []                        # Invierte los elementos de la lista
    for x in range(len(lista) - 1, -1, -1):
        list.append(newList, lista[x])

    print('')
    print("Lista: ", lista)
    print('Largo de la lista: ', len(lista))
    print('Valor máximo: ', max(lista))
    print('Valor mínimo: ', min(lista))
    print('Promedio: ', promedio)
    print('Primer valor de la lista: ', lista[0])
    print('Lista b:', b)
    print('Lista invertida: ', newList)

    # Procesa la lista completa
    for n in lista:
        print(2 * n)

def hacerListas2():
    multiplo2 = list(range(2, 21, 2))
    print(multiplo2)
    print(multiplo2[5:])
    print(multiplo2[:7])
    print(multiplo2[4::4])
    print(multiplo2[3:len(multiplo2)-3])
    print(multiplo2[-1:-len(multiplo2)-1:-1])
    # print(multiplo2[len(multiplo2):0:-1])

def calificarPalindromo():
    palabra = input('Palabra: ')
    original = list(palabra.upper())
    sinEspacios = list.copy(original)
    for repeticion in range(len(sinEspacios)):
        if ' ' in sinEspacios:
            sinEspacios.remove(' ')
    alReves = sinEspacios[-1:-len(sinEspacios)-1:-1]
    if alReves == sinEspacios:
        print(palabra, 'es un palíndromo')
    else:
        print(palabra, 'no es un palíndromo')


def traducirInglesEspañol():
    opcion = 0
    while opcion != 'c':
        print('''
a. Traducir inglés-español
b. Traducir español-ingles
c. Salir''')
        opcion = str(input('¿Qué desea hacer?'))
        if opcion == 'b':
            diccIngEsp = {'perro': 'dog', 'gallina': 'hen', 'pollito': 'chicken', 'pluma': 'pen', 'el': 'the',
                          'libro': 'book', 'lápiz': 'pencil'}
            palabraEspañol = input('Español: ')
            print('Inglés: ', diccIngEsp[palabraEspañol])

    print('Adiós')

hacerListas()