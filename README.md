# 📘 Análisis del proyecto BookBot

Este proyecto consta de dos archivos principales: **`main.py`** y
**`stats.py`**.\
En conjunto, permiten analizar un libro de texto plano (ejemplo:
*frankenstein.txt*) para obtener métricas de palabras y caracteres.

------------------------------------------------------------------------

## 🔹 Archivo `main.py`

### Funcionalidad

-   Punto de entrada del programa.\
-   Valida los argumentos recibidos por línea de comandos (`sys.argv`).\
-   Llama a las funciones de **`stats.py`** para procesar el archivo.

### Flujo principal

1.  Comprueba si se recibe exactamente **1 argumento adicional** (ruta
    al archivo).

    ``` python
    if len(sys.argv) == 2:
    ```

2.  Si el argumento es válido:

    -   Muestra cabecera `"============ BOOKBOT ============"`.
    -   Llama a `count_words_from_text(f_file)` para contar palabras.
    -   Llama a `count_characters_from_text(f_file)` y ordena los
        resultados con `sort_chars_dictionary(...)`.
    -   Imprime las letras y su frecuencia, solo si son alfabéticas
        (`x.isalpha()`).

3.  Si no se recibe el argumento correcto, muestra un mensaje de uso:

        Usage: python3 main.py <path_to_book>

------------------------------------------------------------------------

## 🔹 Archivo `stats.py`

### Funcionalidad

Contiene las funciones auxiliares que hacen el procesamiento de texto:

1.  **`get_book_text(path_to_file)`**
    -   Abre el archivo y retorna todo el contenido como `str`.
    -   Maneja excepciones simples con un `try/except`.
2.  **`count_words_from_text(book)`**
    -   Convierte el contenido en palabras usando `.split()`.
    -   Devuelve el total de palabras o `"NaN"` si el texto no es
        válido.
3.  **`count_characters_from_text(book)`**
    -   Recorre todo el texto y construye un diccionario con el conteo
        de cada carácter (minúsculas).
    -   Incluye letras, espacios, saltos de línea y símbolos.
4.  **`sort_chars_dictionary(chars_dictionary)`**
    -   Recibe un diccionario `{char: count}`.

    -   Lo convierte en una lista de diccionarios con estructura:

        ``` python
        {"char": <caracter>, "num": <cantidad>}
        ```

    -   Ordena la lista en orden descendente por frecuencia.

------------------------------------------------------------------------

## 🔎 Observaciones y Mejoras

-   En `main.py` se usaba `if sys.argv == 2`, lo cual es incorrecto
    porque `sys.argv` es una lista.\
    Debe usarse `len(sys.argv) == 2`.
-   En `main.py`, aunque se recibe un archivo por CLI, siempre analiza
    el `f_file` hardcodeado.\
    Lo correcto sería usar `f_file = sys.argv[1]`.
-   En `stats.py`, `count_words_from_text` devuelve `"NaN"` en caso de
    error. Sería más consistente devolver `0` o `None`.
-   `count_characters_from_text` procesa todo, pero puede fallar si
    `get_book_text` devuelve `None`.
-   Se podría optimizar con `collections.Counter` para simplificar
    conteo de caracteres.

------------------------------------------------------------------------

## 🚀 Ejemplo de uso esperado

``` bash
$ python3 main.py books/frankenstein.txt

============ BOOKBOT ============
Analyzing book found at: books/frankenstein.txt

----------- Word Count ----------
78123 words found in the document!

--------- Character Count -------
'a': 50000
'b': 12345
'c': 6789
...

============= END ===============
```

------------------------------------------------------------------------

## 📂 Conclusión

El proyecto BookBot es un buen ejercicio para: - Practicar manejo de
archivos en Python. - Usar `sys.argv` para parámetros de línea de
comandos. - Implementar conteo de palabras y caracteres. - Ordenar y
filtrar resultados.
