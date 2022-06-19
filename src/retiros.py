def cuenta_a_debitar():
    """
    Esta funcion da a elegir que la cuenta de la que luego se realizara el retiro de dinero.

    Precondicion: 
    Poscondicion: un entero
    """
    #Se da a elegir con que cuenta se tranajara
    cuenta = int(input("Presione 1 y luego ENTER si desea debitar dinero de la caja de ahorros\nPresione 2 y luego ENTER si desea debitar dinero de la cuenta corriente\n"))
    indice = 0
    while cuenta != 1 and cuenta != 2 and indice < 2: #Si la opcion ingresada es erronea
        cuenta = int(input("El valor ingresado no es valido. Ingreselo nuevamente: ")) #Se solicita una nueva opcion
        indice = indice + 1
    if cuenta != 1 and cuenta != 2: #Si luego de todos los intentos posibles la opcion es erronea
        print("El valor ingresado no es valildo. No hay mas intentos") #se avisa
    return cuenta #se retorna la opcion ingresada





def retiros(saldo_pesos, saldo_soles, moneda, cuenta, monto, imprimir):
    """
    Esta es la funcion que se encarga de realizar los retiros de dinero

    Precondicion: dos numeros enteros
    Poscondicion: dos numeros enteros
    """
    if cuenta == 1 or cuenta == 2: #Si se selecciona una cuenta valida
        if moneda == 1: #Si se desean retirar pesos
            if (saldo_pesos - monto) >= 0: #Si el monto es menor al saldo disponible
                saldo_pesos = saldo_pesos - monto #se actualiza el saldo sacandole el monto returado
                if imprimir == "1":
                    with open("voucher.txt", "w") as ticket: #Se registra la operacion en voucher.txt
                        ticket.write(f"Ha retirado {monto} pesos\n")
                        ticket.write(f"Tiene {saldo_pesos} pesos disponibles en su cuenta")
            else: #Si el monto a retirar es mayor al saldo disponible no se realiza ningun movimiento
                print("No posee el saldo suficiente para realizar el retiro")
        elif moneda == 2: #Si se desean retirar soles
            if (saldo_soles - monto) >= 0: #Si el monto es menor al saldo disponible
                saldo_soles = saldo_soles - monto #se actualiza el saldo sacandole el monto retirado
                if imprimir == "1":
                    with open("voucher.txt", "w") as ticket: #Se registra el retiro en el archivo voucher.txt
                        ticket.write(f"Ha retirado {monto} soles\n")
                        ticket.write(f"Tiene {saldo_soles} soles disponibles en su cuenta")
                else: #Si el monto a retirar es mayor al saldo disponible no se realiza ningun movimiento
                    print("No posee el saldo suficiente para realizar el retiro")
                    
            else:
                pass
        else:
            pass
    else:
        pass
    
    return(saldo_pesos, saldo_soles) #Se devuelven los montos actualizados