print(" ")
print("Zamarripa Castro Erick Fabian 3W 1220")
print(" ")

#Inicia una lista para las edades
edades = []

# Solicita al usuario que ingrese 10 edades
for i in range(10):
    edad = int(input(f"Ingrese la edad de la persona {i + 1}: "))
    edades.append(edad) 

#Convierte la lista a una tupla
tupla_edades = tuple(edades)

#Cuenta personas mayores a 20 años
cantidad_superiores_20 = sum(1 for edad in tupla_edades if edad > 20)

print(f"\nCantidad de personas con edades superiores a 20: {cantidad_superiores_20}")