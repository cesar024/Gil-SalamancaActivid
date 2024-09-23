def validar_letras(entrada):
    letras = entrada.split(',')
    letras = [letra.strip() for letra in letras]  # Eliminar espacios en blanco alrededor de cada letra

    for letra in letras:
        if not letra.isalpha():  # Verificar si no es una letra
            return False, f"Error: '{letra}' no es una letra válida."

    if len(letras) != len(set(letras)):  # Comprobar duplicados
        return False, "Error: Las letras no deben estar repetidas."
    if len(letras) == 0:
        return False, "Error: No se ingresaron letras."  
    return True, "Entrada válida."     
intentos = 5

while intentos > 0:
    entrada = input("Ingrese varias letras separadas por comas: ")
    valido, mensaje = validar_letras(entrada)
    
    print(mensaje)  # Mostrar el mensaje de error o de éxito

    if valido:
        break  # Salir del bucle si la entrada es válida
    else:
        intentos -= 1
        print(f"Intentos restantes: {intentos}")

if intentos == 0:
    print("Se han agotado todos los intentos.")
def validar_letras(entrada):
    letras = entrada.split(',')
    letras = [letra.strip() for letra in letras]
    
    if len(letras) == 0:
        return False, "Error: No se ingresaron letras."

    for letra in letras:
        if not letra.isalpha():
            return False, f"Error: '{letra}' no es una letra válida."
    
    if len(letras) != len(set(letras)):
        return False, "Error: Las letras no deben estar repetidas."
    
    return True, "Entrada válida."

intentos = 5

while intentos > 0:
    entrada = input("Ingrese varias letras separadas por comas: ")
    valido, mensaje = validar_letras(entrada)
    
    print(mensaje)

    if valido:
        break
    else:
        intentos -= 1
        print(f"Intentos restantes: {intentos}")

if intentos == 0:
    print("Se han agotado todos los intentos.")