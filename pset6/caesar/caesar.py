# Pset 6 caesar 16/10/2021
from cs50 import *
from string import *

import sys

# Verificamos que el usuario solo introduzca un argumento despues del nombre del programa
if (len(sys.argv) != 2):
    print("¡Eso no es un aspecto de Minecraft, alcornoque!")
    sys.exit(1)

# int(sys.argv) el argumento convierte una cadena a su valor numérico (entero)
key = int(sys.argv[1])

# Solicitamos el texto plano
textoplano = get_string("plaintext: ")
print("ciphertext: ", end="")

i = 0
for i in range(len(textoplano)):
    char = textoplano[i]
    # Verificamos si el formato de texto plano es minuscula o mayuscula segun ascii
    if (char.isupper()):
        # le aplicamos modulo 26 porque son 26 letras del alfabeto ingles
        # Cifrar caracteres en mayusculas
        cifrado = chr((ord(char) + key - 65) % 26 + 65)
        print(cifrado, end="")
    elif(char.islower()):
        # le aplicamos modulo 26 porque son 26 letras del alfabeto ingles
        # Cifrar caracteres en minúscula
        cifrado = chr((ord(char) + key - 97) % 26 + 97)
        print(cifrado, end="")
    else:
        print(char, end="")
print("")
