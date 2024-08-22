# Questions

## What's `stdint.h`?
Es una libreria de C
TODO

## What's the point of using `uint8_t`, `uint32_t`, `int32_t`, and `uint16_t` in a program?
Nos sirven para identificar
Número entero con signo de 1 byte
int16_t
Número entero con signo de 2 bytes
int32_t
Número entero con signo de tamaño igual a un puntero
uint8_t
Número entero sin signo de 1 byte
uint16_t
Número entero sin signo de 2 bytes
uint32_t
SEGUN INTERNET

para definir variables y elementos de un struct con alguna de esas clasificaciones

TODO

## How many bytes is a `BYTE`, a `DWORD`, a `LONG`, and a `WORD`, respectively?

bytes a BYTE Segun internet y yo son lo mismo byte = 8 bits; BYTE = 8 bits
Bytes a DWORD; DWORD = 32 bits es decir 4 bytes
Bytes a LONG; LONG = 32 bits es dedir 4 bytes
Bytes a WORD; WORD = 16 bits es dricr 2 bytes

fuente: https://product-help.schneider-electric.com/Machine%20Expert/V1.1/es/SoMProg/SoMProg/Data_Types/Data_Types-3.htm
TODO

## What (in ASCII, decimal, or hexadecimal) must the first two bytes of any BMP file be? Leading bytes used to identify file formats (with high probability) are generally called "magic numbers."

Bytes	Información
0, 1	Tipo de fichero "BM"
2, 3, 4, 5	Tamaño del archivo
6, 7	Reservado
8, 9	Reservado
10, 11, 12, 13	Inicio de los datos de la imagen
14, 15, 16, 17	Tamaño de la cabecera del bitmap
18, 19, 20, 21	Anchura (píxels)
22, 23, 24, 25	Altura (píxels)
26, 27	Número de planos
28, 29	Tamaño de cada punto
30, 31, 32, 33	Compresión (0=no comprimido)
34, 35, 36, 37	Tamaño de la imagen
38, 39, 40, 41	Resolución horizontal
42, 43, 44, 45	Resolución vertical
46, 47, 48, 49	Tamaño de la tabla de color
50, 51, 52, 53	Contador de colores importantes


TODO

## What's the difference between `bfSize` and `biSize`?
biSize = el tamaño del archivo en bytes de la parte del encabezado de información de un encabezado BMP
bfsize = el tamaño del archivo en bytes del BMP completo (incluido el encabezado y la imagen)
TODO

## What does it mean if `biHeight` is negative?
 Si biHeight es negativo, el mapa de bits es un DIB "de arriba a abajo" y su origen es la esquina superior izquierda.
TODO

## What field in `BITMAPINFOHEADER` specifies the BMP's color depth (i.e., bits per pixel)?
En los archivos BMP, la información de color de cada píxel está codificada en 1, 4, 8, 16 o 24 bits (bits / píxel).
Bits / pixel, también conocido como profundidad de color, es la cantidad máxima de colores en una imagen.
Una imagen a 1 bit / píxel puede tener solo dos colores y a 24 bits / píxel puede tener más de 16 millones de colores diferentes.

Fuente: https://hddrecover.ru/es/android/znachit-bmp-smotret-chto-takoe-bmp-v-drugih-slovaryah-chto-takoe-bmp-format/
TODO

## Why might `fopen` return `NULL` in lines 24 and 32 of `copy.c`?
La funcion fopen
Esta función devuelve un puntero a una FILEque representa el archivo abierto o, en caso de error (como cuando pathnameno existe), NULL.

TODO

## Why is the third argument to `fread` always `1` in our code?
si lee uno chara la vez, sizesería sizeof(char)(es decir, 1) y nmembsería 1.
TODO

## What value does line 63 of `copy.c` assign to `padding` if `bi.biWidth` is `3`?
4
TODO

## What does `fseek` do?
Establece la posición del archivo de la secuencia en el desplazamiento dado .

TODO

## What is `SEEK_CUR`?
mueve la posición del puntero del archivo a la ubicación dada.
TODO
