//25/09/2021
//Pset 4
//Implemente un programa llamado recover que recupere las imágenes JPEG desde una imagen forense
#include <stdio.h>
#include <stdlib.h>
#include <cs50.h>

int main(int argc, char *argv[])
{
    //Revisamos si la cantidad de argumentos esta correcta
    if (argc != 2)
    {
        printf("./recover image \n");
        //retornamos 1
        return 1;
    }

    //fopen - abre un archivo
    FILE *file = fopen(argv[1], "r");

    if (file == NULL)
    {
        printf("No es un archivo\n");
    }

    //Iniciamos contador de archivos
    int jpg_found = 0, filecount = 0;

    //Establecemos el buffer en 512 bytes
    unsigned char buffer[512];

    //Definimos los archivos para imagenes
    FILE *img = NULL;

    //Nombre del archivo
    char filename[8];
    //fread - leer bytes de un archivo
    //direccion, tamaño, cantidad, archivo
    while (fread(buffer, 512, 1, file) == 1)
    {
        //verifica si jpg usando los primeros cuatro bytes
        //Un JPG siempre comienza con alguna de estas secuencias segun el video
        //0xff 0xd8 oxff 0xe0
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {
            //
            if (jpg_found == 1)
            {
                //fclose - cerrar un archivo
                fclose(img);
            }
            else
            {
                jpg_found = 1;
            }
            //sprintf - imprimir en una cadena
            sprintf(filename, "%03i.jpg", filecount);
            //fopen - abre un archivo
            img = fopen(filename, "w");

            filecount++;
        }
        if (jpg_found == 1)
        {
            //fwrite - escribe bytes en un archivo
            fwrite(&buffer, 512, 1, img);
        }

    }
    //Cerramos los archivos
    fclose(file);
    fclose(img);
    return 0 ;
}