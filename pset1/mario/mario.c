// Pset 1
// Este programa recrea una escalera de Super Mario Bros con # como bloques y la altura de la escalera es determinada por el usuario
// Declaramos librerias a usar a lo largo del programa
#include<stdio.h>
#include<cs50.h>

int main(void)
{
    /*Declaramos las variables que usaremos en el programa
    lineas porque con esta variables iteraremos en el bucle que imprimira las lineas
    espacios porque con esta variables iteraremos en el bucle que imprimira los espacios
    altura porque sera la variable que le pediremos al usuario para determinar la altura de la piramide
    */
    int lineas, espacios, altura, numerales;
    // Utilizamos un bucle para solicitar al usuario la altura repetidamente en el caso que la introduzca mal
    do
    {
        // Solitamos al usuario la altura
        printf("ingrese la altura de la piramide \n");
        // La funcion get_int de la libreria cs50 solo acepta numeros enteros
        altura = get_int("Introduzca un numero entre 0 y 23: ");
    }
    while (altura < 0 || altura > 23);
    /* El bucle do while hace que el bloque de codigo que esta dentro de ella repita segun la condicion que se encuentra en el
    while en este caso si el usuario introduce un numero menor a 0 repite el codigo o (Compuesta logica que evalua) la altura es mayor a 23*/

    /* ciclo for para imprimir las lineas
    inicializamos en 0 y llegara hasta 1-que la altura porque es menor a altura
    y por cada iteracion incrementa en 1 las lineas */
    for (lineas = 0; lineas < altura; lineas++)
    {
        /* for para imprimir los espacios de la piramide
        los espacios se imprimiran restando a la altura las lineas y disminuiran en 1
        ## espacios = 2 - 0 = 2 un espacio se imprime un espacio y se resta uno
        ### espacios = 2 - 1 = 1 espacios espacios > 1 por eso no se imprime nada
        */
        for (espacios = altura - lineas; espacios > 1; espacios--)
        {
            printf(" ");

        }
        /* for para los numerales imprime los numerales
        ## numerales= 0 luego 1    lineas= 0 + 2 = 2 condicion numerales menores las lineas + 2 = VERDADERO
        ### numereles = 0 luego 1 luego 2   lineas= 1 + 2 = 3 condicion del for numereles menores a las lineas + 2 = VERDERO*/
        for (numerales = 0; numerales < lineas + 2; numerales++)
        {
            printf("#");
        }
        // imprimimos los saltos de linea
        printf("\n");
    }
}


