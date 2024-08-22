# 26/10/2021
# Pset 6 similarities
# Importamos el modulo nltk.tokenize que nos ayuda a dividir
from nltk.tokenize import sent_tokenize


def lines(a, b):
    """Return lines in both a and b"""
    # El splitlines()método divide una cadena en una lista. La división se realiza en los saltos de línea.
    # A y B contienen las lineas separadas por los saltos de linea
    A = a.splitlines()
    B = b.splitlines()

    # Defino el arreglo que usare
    lista_1 = []
    i = 0
    for i in A:
        if i in B and i not in lista_1:
            # El método append () en Python agrega un solo elemento a la lista existente.
            # No devuelve una nueva lista de elementos, pero modificará la lista original agregando el elemento al final de la lista.
            lista_1.append(i)
        # TODO
    return lista_1


def sentences(a, b):
    """Return sentences in both a and b"""
    # Los tokenizadores dividen las cadenas en listas de subcadenas.
    # Devuelve una copia de texto con token de oración
    A = sent_tokenize(a)
    B = sent_tokenize(b)
    # Declaro el arreglo
    lista_2 = []

    i = 0
    # Este ciclo for determina si i esta en A y esta en B y no esta en la lista_1 agrega en lista 2
    for i in A:
        if i in B and i not in lista_2:
            lista_2.append(i)
        # TODO
    return lista_2


def substrings(a, b, n):
    """Return substrings of length n in both a and b"""
    # Hacemos los arreglos que contendran a y b separadas por palabras
    # El split()método divide una cadena en una lista.
    # Puede especificar el separador, el separador predeterminado es cualquier espacio en blanco.
    A = a.split()
    B = b.split()
    # Definimos variables y arreglos
    lista_3 = []
    Ca = []
    Cb = []
    ia = 0
    ib = 0
    M1 = ""
    M2 = ""
    for ia in A:
        # Si ia no tiene la cantidad n de caracteres no nos sirve
        if len(ia) >= n:
            # pa_0 establece la posicion 0 para el string de longitud n
            for pa_0 in range(len(ia) - n + 1):
                # El rango esta constituido por n elementos
                for k in range(pa_0, n + pa_0, 1):
                    M1 += ia[k]
                # append Descripción: inserta contenido, especificado por el parámetro,
                # al final de cada elemento en el conjunto de elementos coincidentes.
                Ca.append(M1)
                # Reiniciamos M1
                M1 = ""
    # Con el texto B
    for ib in B:
        # Si ia no tiene la cantidad n de caracteres no nos sirve
        if len(ib) >= n:
            # pb_0 establece la posicion 0 para el string de longitud n
            for pb_0 in range(len(ib) - n + 1):
                # El rango esta constituido por n elementos
                for k2 in range(pb_0, n + pb_0, 1):
                    M2 += ib[k2]
                # append Descripción: inserta contenido, especificado por el parámetro,
                # al final de cada elemento en el conjunto de elementos coincidentes.
                Cb.append(M2)
                # Reiniciamos M2
                M2 = ""

    for j in Ca:
        if j in Cb and j not in lista_3:
            lista_3.append(j)
        # TODO
    return lista_3

