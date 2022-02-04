def conversor_a_dolar(moneda,valor_dolar):
    pesos = float(input("¿Cuántos " + moneda + " tienes?: "))
    dolar = str(round((pesos / valor_dolar),2))
    print("Tu tienes $" + dolar + " dólares")

def conversor_a_pesos(moneda,valor_pesos):
    dolares = float(input("¿Cuántos dólares tienes?: "))
    peso = str(round(dolares * valor_pesos,2))
    print("Tu tienes $" + peso + " " + moneda)

menu = """
Bienvenido al conversor de monedas 😁💲

1 - Pesos colombianos a dólares
2 - Pesos mexicanos a dólares 
3 - Pesos argentinos a dólares
4 - Dólares a Pesos Colombianos
5 - Dólares a Pesos Mexicanos
6 - Dólares a Pesos Argentinos

"""

opcion = int(input(menu))

if opcion == 1:
    conversor_a_dolar("COP",3875)
elif opcion == 2:
    conversor_a_dolar("MXN",21)
elif opcion == 3:
    conversor_a_dolar("ARP",65)
elif opcion == 4:
    conversor_a_pesos("COP", 3875)
elif opcion == 5:
    conversor_a_pesos("MXN", 21)
elif opcion == 6:
    conversor_a_pesos("ARP", 65)
else:
    print("Ingresa una opción válida por favor")





