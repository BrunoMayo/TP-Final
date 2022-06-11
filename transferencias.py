from retiros import soles_o_pesos

def transferir(nro_cuenta, saldo_pesos, saldo_soles):
    """
    Esta funcion se encarga de realizar las transferencias

    Preconsicion: 3 numeros enteros
    Poscondicion: 4 numeros enteros y un valor booleano
    """
    
    monto_a_devolver_pesos = 0 #Aca se va a almacenar de ser necesario el dinero a devolver si se ingresa mal el numero de cuenta a transferir
    monto_a_devolver_soles = 0 #Aca se va a almacenar de ser necesario el dinero a devolver si se ingresa mal el numero de cuenta a transferir
    moneda = soles_o_pesos() #Se solicita que se elija el tipo de cambio con el que se va a operar
    cuenta = int(input("Ingrese el numero de cuenta al que le desea transferir: ")) #Se solicita el numero de cuenta a transferir
    if moneda == 1: #Si se decide operar con pesos
        monto = int(input("Ingrese el monto que desea transferir: ")) #Se solicita el monto a transferir
        indice = 0
        while indice < 1 and (saldo_pesos - monto) < 0:
            monto = int(input("Saldo insuficiente. Ingrese un nuevo monto: "))
            indice = indice + 1
        if (saldo_pesos - monto) >= 0: #Si el monto a transferir es menor al saldo disponible
            saldo_pesos = saldo_pesos - monto #Se actualiza el saldo
            monto_a_devolver_pesos = monto #se almacena el monto transferido en caso de que deba ser reintegrado
        else: #Si el monto a transferir es mayor al saldo disponible
            print("No posee el saldo suficiente para realizar la transferencia")
    elif moneda == 2: #Si se desea operar con soles
        monto = int(input("Ingrese el monto que desea retirar: ")) #Se solicita el monto a transferir
        indice = 0
        while indice < 1 and (saldo_soles - monto) < 0: 
            monto = int(input("Saldo insuficiente. Ingrese un nuevo monto: "))
            indice = indice + 1
        if (saldo_soles - monto) >= 0: #Si el monto a transferir es menor al saldo disponible
            saldo_soles = saldo_soles - monto #Se actualiza el saldo
            monto_a_devolver_soles = monto #Se almacena el monto transferido en caso de que deba ser reintegrado
        else: #Si el monto a transferir es mayor al saldo disponible
            print("No posee el saldo suficiente para realizar la transferencia") 

    
    if cuenta == nro_cuenta: #Si la cuenta ingresada es correcta se retorna True
        cuenta = True
    else: #Si la cuenta ingresada es erronea se retorna False y se da aviso
        print("La cuenta a la que le quiere transferir no existe. En 3 dias le reintegraremos el dinero")
        cuenta = False

    return (saldo_pesos, saldo_soles, cuenta, monto_a_devolver_pesos, monto_a_devolver_soles) #Se retornan los saldos actualizados, los montos a devolver y si es necesario devolver


