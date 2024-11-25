print(" ")
print("Zamarripa Castro Erick Fabian 3W 1220")
print(" ")

#Define una lista de nombres
nombres = ["Ana", "Luis", "Alberto", "María", "Alejandra", "Pedro", "Antonio", "Laura", "Adriana", "Jorge"]

#Solicita al usuario que ingrese una letra
letra = input("Ingrese una letra para buscar nombres que comiencen con ella: ").lower()

#Contara cuántos nombres empiezan con la letra elegida
cantidad_nombres = sum(1 for nombre in nombres if nombre.lower().startswith(letra))

print(f"\nCantidad de nombres que comienzan con la letra '{letra}': {cantidad_nombres}")