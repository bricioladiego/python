# contador = 0
# print("2 elevado a " + str(contador) + "es igual a: " + str(2**contador))

# contador = 1
# print("2 elevado a " + str(contador) + "es igual a: " + str(2**contador))

# contador = 2
# print("2 elevado a " + str(contador) + " es igual a: " + str(2**contador))




def run():
    # LIMITE = 1000 #la variable se coloca con mayúscula para indicar que es un valor que no cambia durante la ejecución
    # contador = 0
    # potencia_2 = 2**contador
    # while potencia_2 < LIMITE:
    #    print("2 elevado a " + str(contador) + " es igual a: " + str(potencia_2))
    #    contador = contador + 1 #también se puede poner como contador += 1
    #    potencia_2 = 2**contador
    

     for contador in range (1001):
         print(contador)

    # for potencia_2 in range (11):
    #     contador = 0
    #     contador += 1
    #     potencia_2 = 2**contador
    #     print(potencia_2)
        


if __name__ == "__main__": #entrypoint cuando python encuentra está línea corre lo que esta abajo
    run()

