print(" ")
print("Zamarripa Castro Erick Fabian 3W 1220")
print(" ")

#Solicitar al usuario que ingrese una cadena
cadena = input("Por favor, ingresa una cadena: ")

#Inicia un contador para las mayusculas
contador_mayusculas = 0

#Recorre los carácteres en la cadena
for caracter in cadena:
    #Verifica si el carácter es una letra mayúscula
    if caracter.isupper():
        contador_mayusculas += 1

#Muestra el resultado
print(f"La cadena contiene {contador_mayusculas} letras mayúsculas.")