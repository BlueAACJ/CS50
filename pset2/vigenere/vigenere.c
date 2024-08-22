//Pset 2 Vigenere
//04/09/2021
#include <stdio.h>
#include <cs50.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>

int main(int argc, string argv[])
{
    //Nos aseguramos que el usuario solo introduzca una palabra clave
    if (argc != 2)
    {
        printf("¡Eso no es un aspecto de Minecraft, alcornoque!\n");
        return 1;
    }

    string key = argv[1];
    int tam = strlen(argv[1]);

    //Nos aseguramos que la contrasena no tenga simbolos
    for (int i = 0; i < tam; i++)
    {
        char k = key[i];
        //isalpha comprueba si k es alfabético
        if (!isalpha(k))
        {
            printf("¡Eso no es un aspecto de Minecraft, alcornoque!\n");
            return 1;
        }
    }

    int trans[tam];

    //Establecemos que las letras tenga su valor de dezplazamiento
    //A es 0 dezplazamiento, B es 1 desplazamiento, etc...
    for (int i = 0; i < strlen(argv[1]); i++)
    {
        if (isupper(key[i]))
        {
            trans[i] = key[i] - 65;
        }
        else
        {
            trans[i] = key[i] - 97;
        }
    }

    //Le solicitamos el texto a cifrar
    string textoplano = get_string("plaintext: ");

    printf("ciphertext: ");

    int sigui = 0;
    //Ciframos letra por letra
    for (int j = 0; j < strlen(textoplano); j++)
    {
        if (isalpha(textoplano[j]))
        {
            /*islower comprueba si la letra es una letra mayúscula (de la 'A' a la 'Z') o no.
            En otras palabras, comprueba si el valor ASCII de la letra está entre 65 y 90*/
            if (islower(textoplano[j]))
            {
                if (textoplano[j] + trans[sigui] > 122)
                {
                    //Imprimimos la letra cifrada
                    printf("%c", textoplano[j] + trans[sigui] - 26);
                }
                else
                {
                    //Imprimimos la letra cifrada
                    printf("%c", textoplano[j] + trans[sigui]);

                }
                sigui++;
                if (sigui == tam)
                {
                    sigui = 0;
                }
            }
            //isupper busca una letra mayúscula.
            else if (isupper(textoplano[j]))
            {
                if (textoplano[j] + trans[sigui] > 90)
                {
                    //Imprimimos la letra cifrada
                    printf("%c", (textoplano[j] + trans[sigui]) - 26);
                }
                else
                {
                    //Imprimimos la letra cifrada
                    printf("%c", textoplano[j] + trans[sigui]);

                }
                sigui++;
                if (sigui == tam)
                {
                    sigui = 0;
                }
            }
        }
        else
        {
            printf("%c", textoplano[j]);
        }

    }
    printf("\n");

    return 0;

}
/*
bacon
plaintext: Meet me at the park at eleven am
ciphertext: Negh zf av huf pcfx bt gzrwep oz
*/
