# Pedir al usuario el nombre del archivo de entrada
nombre_archivo = input("Introduce el nombre del archivo de entrada: ")

# Intentar leer el archivo
try:
    archivo = open(nombre_archivo, "r")
    texto = archivo.read()
    archivo.close()
except:
    print("No se pudo leer el archivo.")
    exit()

# Crear un diccionario vacío para almacenar las frecuencias de las letras
frecuencias = {}

# Recorrer cada carácter del texto
for char in texto:
    # Si el carácter es una letra latina, convertirla a minúscula y actualizar el diccionario
    if char.isalpha():
        char = char.lower()
        frecuencias[char] = frecuencias.get(char, 0) + 1

# Ordenar el diccionario por las claves (las letras)
frecuencias = dict(sorted(frecuencias.items()))

# Imprimir el histograma simple
for letra, frecuencia in frecuencias.items():
    print(letra, "*" * frecuencia)
