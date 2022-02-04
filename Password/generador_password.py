import random

def generar_password():
    mayusculas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z']
    minusculas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z']
    simbolos = ['*', '+', '-', '/', '@', '_', '?', '!', '[', '{', '(', ')', '}', ']', ',', ';', '.', '>', '<', '~', '°', '^', '&', '$', '#', '"']
    numeros = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    caracteres = mayusculas + minusculas + simbolos + numeros #genera una tupla con todos los caracteres posibles

    password = [] #genera una lista vacia para colocar los caracteres random

    passwordsize = int(input("¿De que tamaño quieres que sea tu contraseña: ")) 

    for i in range(passwordsize):
        caracter_random = random.choice(caracteres)
        password.append(caracter_random)

    password = "".join(password) #convierte a str la contraseña
    return password


def run():
    password = generar_password()
    print("Tu nueva contraseña es: " + password)


if __name__ == "__main__":
    run()