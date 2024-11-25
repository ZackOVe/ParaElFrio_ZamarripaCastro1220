print(" ")
print("Zamarripa Castro Erick Fabian 3W 1220")
print(" ")

def mas_larga(lista_palabras):
    if not lista_palabras:  #Verifica si la lista está vacía
        return None
    palabra_larga = lista_palabras[0] #Inicia con la primera palabra
    for palabra in lista_palabras:
        if len(palabra) > len(palabra_larga):  #Compara las longitudes
            palabra_larga = palabra
    return palabra_larga

palabras = ["hola", "mundo", "programación", "Python"]
resultado = mas_larga(palabras)
print(f"La palabra más larga es: '{resultado}'")  #Debe imprimir "Programacion"
