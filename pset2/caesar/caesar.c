// pset 2 caesar
// 25/08/2021
#include <stdio.h>
#include <cs50.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>

int main(int argc, string argv[])
{
    //Verificamos que el usuario solo introduzca un argumento despues del nombre del programa
    if (argc != 2)
    {
        printf("¡Eso no es un aspecto de Minecraft, alcornoque!\n");
        return 1;
    }

    //atoi convierte una cadena a su valor numérico (entero)
    int key = atoi(argv[1]);
    //Solicitamos el texto plano
    string textoplano = get_string("plaintext: ");

    printf("ciphertext:");
    //Hacemos el cifrado por cada palabra del texto plano
    //strlen deevuelve la longitud de una cadena de texto
    for (int i = 0; i < strlen(textoplano); i++)
    {
        //Verificamos si el formato de texto plano es minuscula o mayuscula segun ascii
        //Minusculas de 97 a 122
        if ((textoplano[i] >= 97) && (textoplano[i] <= 122))
        {
            //Cifrado va a ser igual a n que es nuestra letra del texto plano sin cifrar a la que le restamos
            // -97 luego le sumamos la llave para mover la cantidad de posiciones que desea el usuario
            //le aplicamos modulo 26 porque son 26 letras del alfabeto ingles
            // y le sumamos 97 para tene la letra cifrada en ascii
            char n = textoplano[i] - 97;
            char cifrado = ((n + key) % 26) + 97;
            printf("%c", cifrado);
        }
        //Verificamos si el formato de texto plano es minuscula o mayuscula segun ascii
        //Mayusculas de 65 a 90
        else if ((textoplano[i] >= 65) && textoplano[i] <= 90)
        {
            char n = textoplano[i] - 65;
            //Cifrado va a ser igual a n que es nuestra letra del texto plano sin cifrar a la que le restamos
            // -65 luego le sumamos la llave para mover la cantidad de posiciones que desea el usuario
            //le aplicamos modulo 26 porque son 26 letras del alfabeto ingles
            // y le sumamos 65 para tene la letra cifrada en ascii
            char cifrado = ((n + key) % 26) + 65 ;
            printf("%c", cifrado);
        }
        else
        {
            printf("%c", textoplano[i]);
        }
    }
    printf("\n");
    return 0;
}
