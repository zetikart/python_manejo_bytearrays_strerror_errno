# Definir la jerarquía de excepciones
class ErrorEntrada(Exception):
    pass

class LineaErronea(ErrorEntrada):
    pass

class ArchivoVacio(ErrorEntrada):
    pass

# Pedir al usuario el nombre del archivo del profesor Jekyll
nombre_archivo = input("Introduce el nombre del archivo del profesor Jekyll: ")

# Intentar leer el archivo
try:
    archivo = open(nombre_archivo, "r")
    lineas = archivo.readlines()
    archivo.close()
    # Si el archivo está vacío, lanzar una excepción
    if len(lineas) == 0:
        raise ArchivoVacio("El archivo está vacío.")
except FileNotFoundError:
    print("No se encontró el archivo.")
    exit()
except ArchivoVacio as e:
    print(e)
    exit()

# Crear un diccionario vacío para almacenar la suma de los puntos de cada estudiante
puntos = {}

# Recorrer cada línea del archivo
for linea in lineas:
    # Separar la línea por espacios
    datos = linea.split()
    # Si la línea no tiene dos elementos, lanzar una excepción
    if len(datos) != 2:
        raise LineaErronea("La línea no tiene el formato correcto.")
    # Obtener el nombre del estudiante y el punto recibido
    nombre = datos[0]
    punto = int(datos[1])
    # Actualizar el diccionario con la suma de los puntos del estudiante
    puntos[nombre] = puntos.get(nombre, 0) + punto

# Ordenar el diccionario por las claves (los nombres de los estudiantes)
puntos = dict(sorted(puntos.items()))

# Imprimir el informe simple
print("Informe de los puntos de los estudiantes:")
for nombre, suma in puntos.items():
    print(nombre, suma)