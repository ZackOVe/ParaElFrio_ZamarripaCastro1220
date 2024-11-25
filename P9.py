print(" ")
print("Zamarripa Castro Erick Fabian 3W 1220")
print(" ")

def contar_vocales(palabra):
    #Inicializa un diccionario
    conteo_vocales = {
        'a': 0,
        'e': 0,
        'i': 0,
        'o': 0,
        'u': 0
    }
    
    #Cuenta las vocales en la palabra
    for letra in palabra.lower():  
        if letra in conteo_vocales:
            conteo_vocales[letra] += 1
            
    return conteo_vocales

#Solicita al usuario que ingrese una palabra
palabra_usuario = input("Ingrese una palabra: ")

#Llama a la función
resultado = contar_vocales(palabra_usuario)

print("\nConteo de vocales:")
for vocal, cantidad in resultado.items():
    print(f"{vocal}: {cantidad}")
