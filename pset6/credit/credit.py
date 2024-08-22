# Pset 6 credit 16/10/2021
from cs50 import *
# numtar al numero de la tarjeta
numtar = get_int("Introduzca el su numero de tarjeta: ")
# Inicializamos y definimos algunas de las variables que usaremos
# dig1 al primer digito de la tarjeta
# dig2 al segundo digito de la tarjeta
# impares a los numeros impares de la tarjeta
# pares a los numeros pares de la tarjeta
dig1 = 0
dig2 = 0
numdig = 0
impares = 0
pares = 0
# La condicion while tiene la funcion de hacer las operaciones de multiplicacion por 2 de los pares y guardar la suma de los impares
while (numtar > 0):
    dig2 = dig1
    dig1 = numtar % 10
    if (numdig % 2 == 0):
        pares = pares + dig1
    else:
        multi = 2 * dig1
        impares += (multi // 10) + (multi % 10)
    numtar = numtar // 10
    numdig = numdig + 1

# Usamos la validacion como un dato boleano para verificar la valides de la tarjeta
if ((pares + impares) % 10 == 0):
    validacion = True
# Aqui determinamos la marca de la tarjeta con los 2 primeros numeros de la tarjeta
validacionmarca = (dig1 * 10) + dig2

if (dig1 == 4 and numdig >= 13 and numdig <= 16 and validacion == True):
    print("VISA")
elif (validacionmarca >= 51 and validacionmarca <= 55 and numdig == 16 and validacion == True):
    print("MASTERCARD")
elif ((validacionmarca == 34 or validacionmarca == 37) and numdig == 15 and validacion == True):
    print("AMEX")
else:
    print("INVALID")
