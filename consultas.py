import random

def soles_o_pesos():
    moneda = int(input("Presione 1 y ENTER si desea operar en Pesos\nPresione 2 y ENTER si desea operar en Soles"))
    indice = 0
    while moneda != 1 and moneda != 2 and indice < 3:
        moneda = int(input("No ha seleccionado una opcion valida. Ingresela nuevamente: "))
        indice = indice + 1
    if moneda != 1 and moneda != 2:
        print("No ha seleccionado una opcion valida. No hay mas intentos")
        moneda = 0    
    return moneda



def saldo_o_movimientos():
    opcion = int(input("Presione 1 y ENTER si desea ve la Posicion Global\nPresione 2 y ENTER si desea consultar sus ultimos movimientos"))
    indice = 0
    while opcion != 1 and opcion != 2 and indice < 3:
        opcion = int(input("No ha seleccionado una opcion valida. Ingresela nuevamente: "))
        indice = indice + 1
    
    if opcion != 1 and opcion != 2:
        print("No ha seleccionado una opcion valida. No hay mas intentos")
        opcion = 0    
    return opcion


def escribir_o_imprimir():
    opcion = int(input("Presione 1 y ENTER si desea visualiza por pantalla\nPresione 2 y ENTER si desea imprimir su ticket"))
    indice = 0
    while opcion != 1 and opcion != 2 and indice < 3:
        opcion = int(input("No ha seleccionado una opcion valida. Ingresela nuevamente: "))
        indice = indice + 1
    if opcion != 1 and opcion != 2:
        print("No ha seleccionado una opcion valida. No hay mas intentos")
        opcion = 0    
    return opcion


def saldo(saldo_pesos, saldo_soles):
    moneda = soles_o_pesos()
    if moneda == 1 or moneda == 2:
        opcion = escribir_o_imprimir()
        if moneda == 1 and opcion == 1:
            print(f"El saldo de la cuenta es de {saldo_pesos} pesos")
        elif moneda == 2 and opcion == 1:
            print(f"El saldo de la cuenta es de {saldo_soles} soles")
        elif moneda == 1 and opcion == 2:
            with open("ticket.txt", "w") as ticket:    
                ticket.write(f"El saldo de la cuenta es de {saldo_pesos} pesos")
        elif moneda == 2 and opcion == 2:
            with open("ticket.txt", "w") as ticket:
                ticket.write(f"El saldo de la cuenta es de {saldo_soles} soles")
        else:
            pass
    else:
        pass
    return (saldo_pesos, saldo_soles)



def movimientos():
    moneda = soles_o_pesos()
    if moneda == 1 or moneda == 2:
        opcion = escribir_o_imprimir()
        if moneda == 1 and opcion == 1:
            indice = 0
            while indice < 5:
                movimiento = random.randint(100, 5000)
                print(f"Se han transferido {movimiento} pesos")
                movimiento = random.randint(100, 5000)
                print(f"Se han depositado {movimiento} pesos")
                indice = indice + 1
        elif moneda == 2 and opcion == 1:
            indice = 0
            while indice < 5:
                movimiento = random.randint(100, 5000)
                print(f"Se han transferido {movimiento} soles")
                movimiento = random.randint(100, 5000)
                print(f"Se han depositado {movimiento} soles")
                indice = indice + 1
        elif moneda == 1 and opcion == 2:
            indice = 0
            with open("ticket.txt", "a") as ticket:
                ticket.truncate(0)
            while indice < 5:
                with open("ticket.txt", "a") as ticket:
                    movimiento = random.randint(100, 5000)
                    ticket.write(f"Se han transferido {movimiento} pesos\n")
                    movimiento = random.randint(100, 5000)
                    ticket.write(f"Se han depositado {movimiento} pesos\n")
                indice = indice + 1
        elif moneda == 2 and opcion == 2:
            indice = 0
            with open("ticket.txt", "a") as ticket:
                ticket.truncate(0)
            while indice < 5:
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
    opcion = saldo_o_movimientos()
    if opcion == 1:
        saldo(saldo_pesos, saldo_soles)
    elif opcion == 2:
        movimientos()
    else:
        print("No ha seleccionado una opcion valida. No hay mas intentos")
    return(saldo_pesos, saldo_soles)