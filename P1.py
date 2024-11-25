print(" ")
print("Zamarripa Castro Erick Fabian 3W 1220")
print(" ")

def max_in_list(numbers):
    if not numbers:
        raise ValueError("La lista no puede estar vacía.")  #Muestra un mensaje en caso no estar permitido

 #Evalua el numero maximo para luego dar el resultado 
    max_number = numbers[0]  
    for number in numbers[1:]:  
        if number > max_number:  
            max_number = number  
    return max_number  

try:
    lista_de_numeros = [3, 5, 1, 8, 2]
    maximo = max_in_list(lista_de_numeros)
    print(f"El número máximo en la lista es: {maximo}")
except ValueError as e:
    print(e)