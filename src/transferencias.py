def monto_a_operar(saldo_pesos, saldo_soles, moneda):
    """
    Esta funcion permite al usuario elegir el monto con el que va a operar basandose en el saldo
    y el tipo de moneda a utilizar

    Precondicion: 3 enteros
    Poscondicion: 1 entero
    """
    if moneda == 1: #Si se decide operar con pesos
        monto = int(input("Ingrese el monto: ")) #Se solicita el monto a transferir
        indice = 0
        while indice < 1 and (saldo_pesos - monto) < 0:
            monto = int(input("Saldo insuficiente. Ingrese un nuevo monto: "))
            indice = indice + 1
    elif moneda == 2: #Si se desea operar con soles
        monto = int(input("Ingrese el monto: ")) #Se solicita el monto a transferir
        indice = 0
        while indice < 1 and (saldo_soles - monto) < 0: 
            monto = int(input("Saldo insuficiente. Ingrese un nuevo monto: "))
            indice = indice + 1
    return monto
    

def transferir(nro_cuenta, saldo_pesos, saldo_soles, moneda, monto, cuenta):
    """
    Esta funcion se encarga de realizar las transferencias

    Preconsicion: 3 numeros enteros
    Poscondicion: 4 numeros enteros y un valor booleano
    """
    
    monto_a_devolver_pesos = 0 #Aca se va a almacenar de ser necesario el dinero a devolver si se ingresa mal el numero de cuenta a transferir
    monto_a_devolver_soles = 0 #Aca se va a almacenar de ser necesario el dinero a devolver si se ingresa mal el numero de cuenta a transferir
    if moneda == 1: #Si se decide operar con pesos
        if (saldo_pesos - monto) >= 0: #Si el monto a transferir es menor al saldo disponible
            saldo_pesos = saldo_pesos - monto #Se actualiza el saldo
            monto_a_devolver_pesos = monto #se almacena el monto transferido en caso de que deba ser reintegrado
        else: #Si el monto a transferir es mayor al saldo disponible
            print("No posee el saldo suficiente para realizar la transferencia")
            monto = False
    elif moneda == 2: #Si se desea operar con soles
        if (saldo_soles - monto) >= 0: #Si el monto a transferir es menor al saldo disponible
            saldo_soles = saldo_soles - monto #Se actualiza el saldo
            monto_a_devolver_soles = monto #Se almacena el monto transferido en caso de que deba ser reintegrado
        else: #Si el monto a transferir es mayor al saldo disponible
            print("No posee el saldo suficiente para realizar la transferencia") 
            monto = False
    
    if cuenta == nro_cuenta: #Si la cuenta ingresada es correcta y se ha intentado transferir un monto posible, se retorna True
        cuenta = True
    elif not monto: #Si la cuenta ingresada es erronea se retorna False y se da aviso
        pass
    else:
        print("La cuenta a la que le quiere transferir no existe. En 3 dias le reintegraremos el dinero")
        cuenta = False

    return (saldo_pesos, saldo_soles, cuenta, monto_a_devolver_pesos, monto_a_devolver_soles) #Se retornan los saldos actualizados, los montos a devolver y si es necesario devolver


