def run():
    # for contador in range(1000):
    #     if contador % 2 != 0:
    #         continue
    #     print(contador)

    # for i in range (10000):
    #     print("Número: " + str(i))
    #     if i == 2904:
    #         break

     texto = input("Escribe un texto: ")
     for letra in texto:
         if letra == "ñ":
             break
         print(letra)

if __name__ == "__main__":
    run()