// Implements a dictionary's functionality
/*
pset5 09/10/2021*/
#include <stdint.h>
#include <stdbool.h>
#include <stdlib.h>
#include <stdio.h>
#include <cs50.h>
#include <ctype.h>
#include <string.h>
#include <strings.h>

#include "dictionary.h"

//Constante tamano del hash con la palabra mas grande y el tamano de la letra mas grande del abecedario
const unsigned int hashtable_tam = ((LENGTH + 1) * 'z');


// Define la estructura de un nodo
typedef struct nodo
{
    char word[LENGTH + 1];
    struct nodo *next;
} nodo;

nodo *hashtable[hashtable_tam];
//inicializamos contador
int contador = 0;

unsigned int hash(const char *word)
{
    int sum = 0;
    //strlen - calcula la longitud de una cadena
    for (int i = 0; i < strlen(word); i++)
    {
        //tolower - convertir chara en minúsculas
        sum += tolower(word[i]) ;
    }
    return (sum % hashtable_tam);
}

// Loads dictionary into memory, returning true if successful else false
bool load(const char *dictionary)
{
    // TODO
    //fopen - abre un archivo
    FILE *file = fopen(dictionary, "r");
    if (file == NULL)
    {
        return false;
    }
    char word[LENGTH + 1];

    while (fscanf(file, "%s", word) != EOF)
    {
        //malloc : asigna memoria dinámicamente
        //Al nuevo nodo
        nodo *nuevo_nodo = malloc(sizeof(nodo));
        if (nuevo_nodo == NULL)
        {
            return false ;
        }
        //strcpy - copiar una cadena
        strcpy(nuevo_nodo->word, word);
        nuevo_nodo ->next = NULL;
        int indice = hash(word);

        if (hashtable[indice] == NULL)
        {
            hashtable[indice] = nuevo_nodo;
        }
        else
        {
            nuevo_nodo -> next = hashtable[indice];
            hashtable[indice] = nuevo_nodo;
        }
        //Sumammos al contador de palabras
        contador++;
    }
    // CErramos archivo
    fclose(file);
    return true;
}

// Returns true if word is in dictionary else false
// Devuelve verdadera si la palabra está en el diccionario más falsa
bool check(const char *word)
{
    // TODO
    // Sacamos el indice del hash
    int indice = hash(word);
    nodo *cursor = hashtable[indice];
    while (cursor != NULL)
    {
        //strcasecmp - compara dos cadenas ignorando mayúsculas y minúsculas
        if (strcasecmp(cursor->word, word) == 0)
        {
            return true;
        }
        cursor = cursor -> next;
    }
    return false;
}

// Returns number of words in dictionary if loaded else 0 if not yet loaded
unsigned int size(void)
{
    // TODO
    //Retornamos el contador de palabras
    return contador;

}


// Unloads dictionary from memory, returning true if successful else false
bool unload(void)
{
    // CIclo for del tamano del hash
    for (int i = 0; i < hashtable_tam; i++)
    {
        nodo *head = hashtable[i];
        nodo *cursor = head ;
        nodo *tmp = head;
        while (cursor != NULL)
        {
            cursor = cursor -> next;
            //free : libera memoria asignada dinámicamente
            free(tmp);
            tmp = cursor ;

        }
    }
    return true ;
}
