try:
    stream = open("C:/Users/PC RST/OneDrive/Escritorio/jola.txt", "rt")
    # El procesamiento va aquí.
    stream.close()
except Exception as exc:
    print("No se puede abrir el archivo:", exc)
