# Pset 6 cash 16/10/2021
from cs50 import *
# Iniciamos el contador de monedas y el cambio
cambio = 0
nmonedas = 0

cambio = get_float("ingrese el cambio a dar: ")
# Este ciclo se asegura que el usuario introduzca un numero positivo
while(cambio < 0):
    cambio = get_float("ingrese el cambio a dar: ")

# Redondeo para eliminar cualquier tipo de imprecision
cambio = (cambio * 100)
print(f"su cambio en centavos es: {cambio}")

while (cambio >= 25):
    nmonedas = nmonedas + 1
    cambio = cambio - 25
# Este ciclo determina el numero de monedas de 10 a usar para el cambio
while (cambio >= 10):
    nmonedas = nmonedas + 1
    cambio = cambio - 10

# Este ciclo determina el numero de monedas de 5 a usar para el cambio
while (cambio >= 5):
    nmonedas = nmonedas + 1
    cambio = cambio - 5
# Este ciclo determina el numero de monedas de 1 a usar para el cambio
while (cambio >= 1):
    nmonedas = nmonedas + 1
    cambio = cambio - 1
# Monstramos el numero de monedas
print(f"El numero minimo de monedas que se puede dar de cambio es:{nmonedas}")
