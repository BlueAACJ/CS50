# Pset 6 vigenere 16/10/2021
from cs50 import *
from string import *

import sys

# Verificamos que el usuario solo introduzca un argumento despues del nombre del programa
if (len(sys.argv) != 2):
    print("¡Eso no es un aspecto de Minecraft, alcornoque!")
    sys.exit()

key = (sys.argv[1])
tam = (len(sys.argv[1]))
i = 0
# Nos aseguramos que la contrasena no tenga simbolos
for i in range(tam):
    k = key[i]
    # isalpha comprueba si k es alfabético
    if(key[i].isalpha() == False):
        print("¡Eso no es un aspecto de Minecraft, alcornoque!")
        sys.exit()

i = 0
trans = []
for i in range(len(sys.argv[1])):
    c = key[i]
    if(c.isupper()):
        trans.append(ord(c) - 65)
    elif(c.islower()):
        trans.append(ord(c) - 97)

textoplano = get_string("plaintext: ")
print("ciphertext: ", end="")
sigui = 0
j = 0
for j in range(len(textoplano)):
    char = textoplano[j]
    if (char.isalpha()):
        # islower comprueba si la letra es una letra mayúscula (de la 'A' a la 'Z') o no.
        # En otras palabras, comprueba si el valor ASCII de la letra está entre 65 y 90
        if (char.islower()):
            if (ord(char) + trans[sigui] > 122):
                # Imprimimos la letra cifrada
                print(chr(ord(char) + trans[sigui] - 26), end="")
            else:
                # Imprimimos la letra cifrada
                print(chr(ord(char) + trans[sigui]), end="")
            sigui = sigui + 1
            if (sigui == tam):
                sigui = 0
            # isupper busca una letra mayúscula.
        elif (char.isupper()):
            if (ord(char) + trans[sigui] > 90):
                # Imprimimos la letra cifrada
                print(chr(ord(char) + trans[sigui] - 26), end="")
            else:
                # Imprimimos la letra cifrada
                print(chr(ord(char) + trans[sigui]), end="")
            sigui = sigui + 1
            if (sigui == tam):
                sigui = 0
    else:
        print(char, end="")
