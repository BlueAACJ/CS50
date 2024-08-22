# Questions
Preguntas

## What is pneumonoultramicroscopicsilicovolcanoconiosis?
¿Qué es la neumonoultramicroscópicosilicovolcanoconiosis?

el término utilizado para referirse a la enfermedad pulmonar producida por la intoxicación de sílice
Y en el programa es la palabra mas grande
En dictionary.h dice Longitud máxima de una palabra y como ejemplo neumonoultramicroscópicosilicovolcanoconiosis


## According to its man page, what does `getrusage` do?
Según su página de manual, ¿qué hace `getrusage`?

obtener el uso de recursos

## Per that same man page, how many members are in a variable of type `struct rusage`?
Según esa misma página de manual, ¿cuántos miembros hay en una variable de tipo `struct rusage`?

struct rusage {
    struct timeval ru_utime; /* user CPU time used */ tiempo de CPU de usuario utilizado
    struct timeval ru_stime; /* system CPU time used */ tiempo de CPU del sistema utilizado
    long   ru_maxrss;        /* maximum resident set size */ tamaño máximo del conjunto residente
    long   ru_ixrss;         /* integral shared memory size */ tamaño de memoria compartida integral
    long   ru_idrss;         /* integral unshared data size */ tamaño de datos integrales no compartidos
    long   ru_isrss;         /* integral unshared stack size */ tamaño de pila integral no compartido
    long   ru_minflt;        /* page reclaims (soft page faults) */ reclamaciones de página (fallos de página suaves)
    long   ru_majflt;        /* page faults (hard page faults) */ fallas de página (fallas de página fuerte)
    long   ru_nswap;         /* swaps */ intercambios
    long   ru_inblock;       /* block input operations */ bloquear operaciones de entrada
    long   ru_oublock;       /* block output operations */ operaciones de salida de bloque
    long   ru_msgsnd;        /* IPC messages sent */ Mensajes de IPC enviados
    long   ru_msgrcv;        /* IPC messages received */ Mensajes de IPC recibidos
    long   ru_nsignals;      /* signals received */ señales recibidas
    long   ru_nvcsw;         /* voluntary context switches */ cambios de contexto voluntarios
    long   ru_nivcsw;        /* involuntary context switches */ cambios de contexto involuntarios
};

## Why do you think we pass `before` and `after` by reference (instead of by value) to `calculate`,
## even though we're not changing their contents?
¿Por qué crees que pasamos "before" y "after" por referencia (en lugar de por valor) a "calculate",
aunque no estemos cambiando su contenido?

Pasamos before y after por referencia porque pasar estructuras grandes por valor es lento y ocupa mucha memoria

## Explain as precisely as possible, in a paragraph or more, how `main` goes about reading words from a file.
## In other words, convince us that you indeed understand how that function's `for` loop works.
Explique con la mayor precisión posible, en un párrafo o más, cómo funciona "main" en la lectura de palabras de un archivo.
En otras palabras, convéncenos de que realmente comprende cómo funciona el ciclo "for" de esa función.

El for  "for (int c = fgetc(file); c != EOF; c = fgetc(file))"
La funcion fgetc () lee el siguiente carácter de streamy lo devuelve como una unsigned char conversión a un int, o EOF al final del archivo o error.
Al obtener el siguiente caracter avanza el indicador de posicion hasta el final del archivo EO.
Cada que recibe caracter lo evalua en varios if else a lo largo del for.
El if: if (isalpha(c) || (c == '\'' && index > 0)) revisa si el caracter es alfabetico o un apostrofe
el else if : else if (isdigit(c)) con la funcion isdigit: comprueba si un carácter es un dígito numerico
el else if (index > 0) identifica si es un espacio o punto, asi saber si encontramis una palabra


## Why do you think we used `fgetc` to read each word's characters one at a time rather than use `fscanf`
## with a format string like `"%s"` to read whole words at a time? Put another way, what problems might arise by relying on `fscanf` alone?
¿Por qué crees que usamos `fgetc` para leer los caracteres de cada palabra uno a la vez en lugar de usar` fscanf` con una cadena de formato como `"% s "`
para leer palabras completas a la vez? Dicho de otra manera, ¿qué problemas pueden surgir si se confía únicamente en `fscanf`?

fgetc () lee el siguiente carácter de streamy lo devuelve como una unsigned charconversión a un int, o EOF al final del archivo o error.
fscanf: obtiene la entrada de un archivo

El fscanf lee los caracteres hasta encontrar un espacio en blanco como en los archivos de texto terminan en punto el programa los puede interpretar
como una palabra completa.


## Why do you think we declared the parameters for `check` and `load` as `const` (which means "constant")?
¿Por qué crees que declaramos los parámetros para `check` y` load` como `const` (que significa" constante ")?

Constante significa que es un valor que no cambia a lo largo del programa.
En diccionary.c declaramos check y load como constante porque asi evitamos cambios en la cadena a la que apuntamos.
Dicho de otra forma las declaramos constantes para evitar cambios en la palabra leida.
