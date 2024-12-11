
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

# Ordenar el diccionario por los valores (las frecuencias) de mayor a menor
frecuencias = dict(sorted(frecuencias.items(), key=lambda x: x[1], reverse=True))

# Crear el nombre del archivo de salida con la extensión '.hist'
nombre_salida = nombre_archivo + ".hist"

# Intentar escribir el archivo de salida
try:
    salida = open(nombre_salida, "w")
    # Imprimir el histograma simple en el archivo
    for letra, frecuencia in frecuencias.items():
        salida.write(letra + " " + "*" * frecuencia + "\n")
    salida.close()
    print("El histograma se ha guardado en el archivo", nombre_salida)
except:
    print("No se pudo escribir el archivo de salida.")
