# pset 6 mario
from cs50 import *

# Saludamos y explicamos en que consiste el programa
altura = -1
# Sustituimos el do-while por un while
while altura < 0 or altura > 23:
    print("Este programa dibujara una escalera al estilo de Mario Bros con # ")
    altura = get_int("Introduzaca un número entre 0 y 23 para dibujar la escalera: ")

numerales = 0
linea = 0
# Hacemos un ciclo for para los saltos de linea
for linea in range(1, altura + 1, 1):
    # For para los espacios
    for espacios in range(0, altura - linea, 1):
        print(" ", end="")
    # For para imprimir los numerales
    for numerales in range(0, linea + 1, 1):
        print("#", end="")
    # Saltos de linea
    print("\n", end="")
