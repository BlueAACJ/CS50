// Pset 1
// Este programa determina el numero minimo de monedas requeridas para dar el cambio al usuario
// declaramos librerias a usar
#include<stdio.h>
#include<cs50.h>
#include<math.h>

int main(void)
{
    //declaramos e inicializamos variables a usar en el programa
    float cambio;
    int nmonedas = 0;
    // cambio es el vuelto a dar y nmonedas es el contador de monedas

    // Usamos un bucle do while para repetir una parte del codigo hasta que el usuario introduzca una opcion valida
    do
    {
        // con la funcion get_float hacemos que el usario solo pueda introducir un numero flotante
        cambio = get_float("ingrese el cambio a dar :");
        // con el cambio < 0 hacemos que se repita hasta que introduzca un numero flotante positivo
    }
    while (cambio < 0);

    // redondamos el cambio para evitar impresiciones
    // funcion round() en C devuelve el valor entero más cercano del argumento float / double / long double pasado a esta función.
    cambio = round(cambio * 100);

    /*con los siguientes ciclos contamos el numero de monedas minimo a usar para el cambio de cliente empezando por 25
    luego 10 luego 5 y por ultimo 1 haciendo algo asi
    cambio = 60
    cambio - 25= 45
    cambio - 25= 20
    cambio - 10=10
    cambio - 10=0
    para que sea el minimo numero posible*/
    // bucle while para que se ejecute mientras la condicion sea cierta
    while (cambio >= 25)
    {
        // aumenta el numero de monedas +1 porque se esta usando una moneda el valor de la condicion
        nmonedas++;
        // Le damos el nuevo valor al cambio
        cambio = cambio - 25;
    }
    while (cambio >= 10)
    {
        // aumenta el numero de monedas +1 porque se esta usando una moneda el valor de la condicion
        nmonedas++;
        // Le damos el nuevo valor al cambio
        cambio = cambio - 10;
    }
    while (cambio >= 5)
    {
        // aumenta el numero de monedas +1 porque se esta usando una moneda el valor de la condicion
        nmonedas++;
        // Le damos el nuevo valor al cambio
        cambio = cambio - 5;
    }
    while (cambio >= 1)
    {
        // aumenta el numero de monedas +1 porque se esta usando una moneda el valor de la condicion
        nmonedas++;
        // Le damos el nuevo valor al cambio
        cambio = cambio - 1;
    }
    // Imprimimos el numero de monedas minimos para dear el cambio
    printf("%d \n", nmonedas);

    return 0;
}
