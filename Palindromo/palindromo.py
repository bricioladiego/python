def palindromo (palabra): #define la función 
    palabra = palabra.replace(" ","") #quita los espacios
    palabra = palabra.upper() #transforma todo a mayúsculas (se puede usar en minúsculas)
    palabra_invertida = palabra[::-1] #metodo para invertir la frase o palabra
    if palabra == palabra_invertida: #compara ambas palabras
        return True #regresa el valor verdadero a la variable "es_palindromo"
    else:
        return False

def run(): #run o main se usan como función principal en las buenas prácticas
    palabra = input("Escribe una frase o una palabra: ") #solicita la frase a evaluar
    es_palindromo = palindromo(palabra) #guarda en la variable el resultado de la función
    if es_palindromo == True: 
        print("Es un palindromo")
    else:
        print("No es un palindromo")

if __name__ == "__main__": #entrypoint cuando python encuentra está línea corre lo que esta abajo
    run()
    

    