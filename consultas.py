import random

def soles_o_pesos():
    """
    Esta funcion se encarga de dar a elegir con que tipo de cambio se va a operar

    Precondicion: 
    Poscondicion: un numero entero 
    """
    #Se da a elegir que tipo de cambio se va a utilizar
    moneda = int(input("Presione 1 y ENTER si desea operar en Pesos\nPresione 2 y ENTER si desea operar en Soles\n"))
    indice = 0
    while moneda != 1 and moneda != 2 and indice < 3: #Si se elije una opcion invalida
        moneda = int(input("No ha seleccionado una opcion valida. Ingresela nuevamente: ")) #Se solicita que se ingrese una nueva opcion
        indice = indice + 1
    if moneda != 1 and moneda != 2: #Si luego de los intentos la opcion sigue siendo invalida
        print("No ha seleccionado una opcion valida. No hay mas intentos") #Se da aviso
    return moneda #Se retorna la ultima opcion



def saldo_o_movimientos():
    """
    Esta funcion se encarga de dar a elegir que operacion se quiere realizar
    """
    #Se da a elegir que tipo de operacion realizar
    opcion = int(input("Presione 1 y ENTER si desea ve la Posicion Global\nPresione 2 y ENTER si desea consultar sus ultimos movimientos\n"))
    indice = 0
    while opcion != 1 and opcion != 2 and indice < 3: #Si la opcion ingresada no es valida
        opcion = int(input("No ha seleccionado una opcion valida. Ingresela nuevamente: ")) #Se solicita que se ingrese una opcion nuevamente
        indice = indice + 1
    if opcion != 1 and opcion != 2: #Si al final de todos los intentos la opcion sigue siendo invalida
        print("No ha seleccionado una opcion valida. No hay mas intentos") #Se da aviso
    return opcion #Se retorna la ultima opcion ingresada


def escribir_o_imprimir():
    """
    Esta funcion se encarga de dar a elegir entre imprimir en pantalla o en un archivo txt
    
    Precondicion:
    Poscondicion: un numero entero
    """
    #Se da a elegir que opcion se desea realizar
    opcion = int(input("Presione 1 y ENTER si desea visualiza por pantalla\nPresione 2 y ENTER si desea imprimir su ticket\n"))
    indice = 0
    while opcion != 1 and opcion != 2 and indice < 3: #Si la opcion elegidaa no es valida
        opcion = int(input("No ha seleccionado una opcion valida. Ingresela nuevamente: ")) #Se solicita que se ingrese una opcion nuevamente
        indice = indice + 1
    if opcion != 1 and opcion != 2: #Si luego de todos los intentos la opcion sigue siendo invalida
        print("No ha seleccionado una opcion valida. No hay mas intentos") #Se da aviso
    return opcion #Se devuelve la ultima opcion ingresada


def saldo(saldo_pesos, saldo_soles):
    """
    Esta funcion es la encargada de devolver el saldo en el formato que se desee

    Precondicion: dos numeros enteros
    Poscondicion: dos numeros enteros
    """
    moneda = soles_o_pesos() #Se da a elegir que tipo de cambio se va a utilizar
    if moneda == 1 or moneda == 2: #Si se elige un tipo de cambio permitido
        opcion = escribir_o_imprimir() #Se da a elegir como se desea mostrar
        if moneda == 1 and opcion == 1: #Si se eligen pesos e imptimir por pantalla
            print(f"El saldo de la cuenta es de {saldo_pesos} pesos") #Se imprime el saldo en pesos por pantalla
        elif moneda == 2 and opcion == 1: #Si se eligen soles e imprimir por pantalla 
            print(f"El saldo de la cuenta es de {saldo_soles} soles") #Se imprime el saldo en soles por pantalla
        elif moneda == 1 and opcion == 2: # Si se eligen pesos e imprimir en un archivo
            with open("ticket.txt", "w") as ticket: #Se imprime el saldo en pesos en el archivo ticket.txt
                ticket.write(f"El saldo de la cuenta es de {saldo_pesos} pesos")
        elif moneda == 2 and opcion == 2: #Si se eligen soles e imprimir en un archivo
            with open("ticket.txt", "w") as ticket: #Se imprime el saldo en soles en el archivo ticket.txt
                ticket.write(f"El saldo de la cuenta es de {saldo_soles} soles")
        else:
            pass
    else:
        pass
    return (saldo_pesos, saldo_soles) #Se devuelve el saldo en pesos y soles



def movimientos():
    """
    Esta funcion se encarga de generar 10 movimientos e imprimirlos en el tipo de cambio y forma que se elija

    Precondicion:
    Poscondicion:
    """
    moneda = soles_o_pesos() #Se da a elegir el tipo de cambio a usar
    if moneda == 1 or moneda == 2: #si se elige un tipo de cambio valido
        opcion = escribir_o_imprimir() #Se da a elegir como visualizar los movimientos
        if moneda == 1 and opcion == 1: #Si se eligen pesos y visualizar por pantalla
            indice = 0
            while indice < 5: #Se generan e imprimen por pantalla 5 depositos y 5 transferencias aleatorias en pesos
                movimiento = random.randint(100, 5000)
                print(f"Se han transferido {movimiento} pesos")
                movimiento = random.randint(100, 5000)
                print(f"Se han depositado {movimiento} pesos")
                indice = indice + 1
        elif moneda == 2 and opcion == 1: #Si se eligen soles e imprimir por pantalla
            indice = 0
            while indice < 5: #Se generan e imprimen por pantalla 5 depositos y 5 transferencias aleatorias en soles
                movimiento = random.randint(100, 5000)
                print(f"Se han transferido {movimiento} soles")
                movimiento = random.randint(100, 5000)
                print(f"Se han depositado {movimiento} soles")
                indice = indice + 1
        elif moneda == 1 and opcion == 2: #Si se eligen pesos e imprimir en archivo
            indice = 0
            with open("ticket.txt", "a") as ticket: #Se borra la informacion que exista en el archivo ticket.txt
                ticket.truncate(0)
            while indice < 5: #Se generan 5 depositos y 5 transferencias en pesos aleatoriamente y se imprimen en ticket.txt
                with open("ticket.txt", "a") as ticket:
                    movimiento = random.randint(100, 5000)
                    ticket.write(f"Se han transferido {movimiento} pesos\n")
                    movimiento = random.randint(100, 5000)
                    ticket.write(f"Se han depositado {movimiento} pesos\n")
                indice = indice + 1
        elif moneda == 2 and opcion == 2: #Si se eligen soles e imprimir en archivo
            indice = 0
            with open("ticket.txt", "a") as ticket: #Se borra el contenido de ticket.txt
                ticket.truncate(0)
            while indice < 5: #Se generan 5 depositos y 5 transferencias aleatoriamente y se imprimern en ticket.txt
                with open("ticket.txt", "a") as ticket:
                    movimiento = random.randint(100, 5000)
                    ticket.write(f"Se han transferido {movimiento} soles\n")
                    movimiento = random.randint(100, 5000)
                    ticket.write(f"Se han depositado {movimiento} soles\n")
                indice = indice + 1
        else:
            pass
    else:
        pass
    return None


def consultas(saldo_pesos, saldo_soles):
    """
    Esta funcion se encarga de unir las funciones que componen a las consultas

    Precondicion: dos numeros enteros
    Poscondicion: dos nuemros enteros
    """
    opcion = saldo_o_movimientos() #Se da a elegir que operacion se desea consultar, si el saldo o los ultimos movimientos
    if opcion == 1: #Si se desea visualizar el saldo
        saldo(saldo_pesos, saldo_soles) #se llama a la funcion encargada de eso
    elif opcion == 2: #Si se desean visualizar los movimientos
        movimientos() #Se llama a ala funcion encargada de eso
    else: #Si se elie una opcion no valida 
        print("No ha seleccionado una opcion valida. No hay mas intentos") #Se da aviso
    return(saldo_pesos, saldo_soles) #Se retornan los saldos