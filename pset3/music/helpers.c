// Helper functions for music

/*
pset 3 music */
#include <cs50.h>
#include <stdio.h>
#include <math.h>
#include <string.h>
#include <stdlib.h>
#include "helpers.h"

// Converts a fraction formatted as X/Y to eighths
int duration(string fraction)
{
    int x = atoi(&fraction[0]);
    int y = atoi(&fraction[2]);
    //Convertirla a un número entero de octavos corcheas
    int duracion = (8 / y) * x;

    return duracion;
}

// Calculates frequency (in Hz) of a note
int frequency(string note)
{
    int octava, n = 0;
    if (strlen(note) == 3)
    {
        //atoi - convierte una cadena(string) en un int
        octava = atoi(&note[2]);
        char alteraciones = note[1];
        /*El efecto de # y b, también conocidos como alteraciones,
        es aumentar o disminuir respectivamente, el tono de una nota en un semitono.*/
        if (alteraciones == '#')
        {
            n += 1;
        }
        else if (alteraciones == 'b')
        {
            n -= 1;
        }
    }
    else
    {
        //atoi - convierte una cadena(string) en un int
        octava = atoi(&note[1]);

    }
    char letra = note[0];

    if (letra == 'A')
    {
        n += 0;
    }
    else if (letra == 'B')
    {
        n += 2;
    }
    else if (letra == 'C')
    {
        n -= 9;
    }
    else if (letra == 'D')
    {
        n -= 7;
    }
    else if (letra == 'E')
    {
        n -= 5;
    }
    else if (letra == 'F')
    {
        n -= 4;
    }
    else if (letra == 'G')
    {
        n -= 2;
    }
    n += (octava - 4) * 12;
    float k = n / 12. ;
    float f = round(pow(2, k) * 440);

    return f;
}

// Determines whether a string represents a rest
bool is_rest(string s)
{
    /*strcmp - compara dos cadenas
    en este caso comparamos s con espacio que se reconoce como ""
    retornamos true si es verdadero y false si es falso */
    if (strcmp(s, "") == 0)
    {
        return true;
    }
    else
    {
        return false;
    }
}
