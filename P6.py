print(" ")
print("Zamarripa Castro Erick Fabian 3W 1220")
print(" ")

#Solicita el año
año_actual = int(input("Ingrese el año en curso: "))

#Inicializa una lista para almacenar la información 
personas = []

#Ingresa información de tres personas
for i in range(3):
    nombre = input(f"Ingrese el nombre de la persona {i + 1}: ")
    año_nacimiento = int(input(f"Ingrese el año de nacimiento de {nombre}: "))
    edad = año_actual - año_nacimiento  # Calcular la edad
    personas.append((nombre, edad))  # Agregar a la lista

#Imprimir la edad que cumplirán
print("\nAños que cumplirán durante el año en curso:")
for nombre, edad in personas:
    print(f"{nombre} cumplirá {edad} años.")