// Pset 1
// Declaramos librerias
#include<stdio.h>
#include<cs50.h>
#include<stdlib.h>

int main(void)
{
    /* declaramos variable a usar numtar el cual es el numero de tarjeta que el usuario introduzca lo declaramos como long long por el tama;o del
    numero de tarjeta*/
    // get_long_long es parte de la libreria de cs50 el cual pide al usuario un numero entero grande
    long long numtar = get_long_long("INtroduzca el numero de tarjeta: ");
    int dig1 = 0, dig2 = 0, numdig = 0, pares = 0, impares = 0;
    /*declaramos las variables
    dig1 porque es el primer digito de la tarjeta llendo de otras hacia adelante
    dig2 porque es el segundo digito de la tarjeta llendo de otras hacia adelante
    numdig para contar el numero de digitos para la validacion del final sobre la marca de la tarjeta
    pares para almacenar el valor de los numero pares de la tarjeta para la validacion en el caso que exista la tarjeta
    impares para almacenar el valor de los numero pares de la tarjeta para la validacion en el caso que exista la tarjeta

    Creamos un bucle while para acceder a cada numero de la tarjeta y hacer las operaciones con los pares e impares */
    while (numtar > 0)
    {
        // Le asignamos el valor de dig1 a dig2 para validar los 2 primeros numeros de la tarjeta
        dig2 = dig1;
        // 378282246310005 mod 10 = 5 accedemos al primer digito de la tarjeta de atras hacia adelante
        // 37828224631000.5 mod 10 = 0.5 accedemos al segundo digito de la tarjeta de atras hacia adelante
        dig1 = numtar % 10;

        if (numdig % 2 == 0)
        {
            //sumamos los numeros impares
            impares += dig1 ;
        }
        else
        {
            // mutiplicamos por 2 los numeros pares
            int multi = 2 * dig1;
            /* Sumamos lo digitos individuales
            Ejemplo 14
            14 / 10 = 1.4 redondeado a 1
            14 % 10 = 4
            */
            pares += (multi / 10) + (multi % 10);
        }
        // reasiganmos un nuevo valor al numero de tarjeta dividiendo por 10 para acceder al siguiente digito
        // Ejemplo 378282246310005 / 10 = 37,828,224,631,000.5
        numtar /= 10;
        // sumamos un numero de digito para la validacion de la marca
        numdig++;
    }
    // Validadion booleana para verificar si la tarjeta es "real"  si esta validacion es falsa marcaremos la tarjeta como invalida
    bool validacion = (pares + impares) % 10 == 0;
    /* Validamos la marca de la tarjeta con los 2 primeros digitos de la tarjeta
     multiplicamos * 10 el primer digito para hacerlo decema ya que por las operaciones anteriores es una unidad
    y sumamos dig2 para hacer el numero completo
     ejemplo validacionmarca = (3 * 10) + 7 = 37*/
    int validacionmarca = (dig1 * 10) + dig2;

    if (dig1 == 4 && numdig >= 13 && numdig <= 16 && validacion)
    {
        printf("VISA\n");
    }
    else if (validacionmarca >= 51 && validacionmarca <= 55 && numdig == 16 && validacion)
    {
        printf("MASTERCARD\n");
    }
    else if ((validacionmarca == 34 || validacionmarca == 37) && numdig == 15 && validacion)
    {
        printf("AMEX\n");
    }
    else
    {
        printf("INVALID\n");
    }
    return 0;
}
