print(" ")
print("Zamarripa Castro Erick Fabian 3W 1220")
print(" ")

#Solicita al usuario que ingrese un número binario
numero_binario = input("Por favor, ingresa un número binario: ")

#Verifica si es un número binario válido
if all(bit in '01' for bit in numero_binario):
    #Hace el número binario a entero
    numero_entero = int(numero_binario, 2)
    #Muestra el resultado
    print(f"El número binario {numero_binario} es igual a {numero_entero} en decimal.")
else:
    print("Error: La entrada no es un número binario válido.")