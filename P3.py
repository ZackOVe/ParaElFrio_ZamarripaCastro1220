print(" ")
print("Zamarripa Castro Erick Fabian 3W 1220")
print(" ")

def filtrar_palabras(lista_palabras, n):
    return [palabra for palabra in lista_palabras if len(palabra) > n]

#Mostrara toda la linea de texto 10
if __name__ == "__main__":
    lista = ["hola", "mundo", "programación", "Python", "función", "red"]
    n = 5
    resultado = filtrar_palabras(lista, n)
    print(resultado)  