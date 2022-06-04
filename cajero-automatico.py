from time import sleep


#clave = 12345
#dni = 12345678
#numero de cuenta = 98765
#saldo en ars = 85000
#saldo en soles = 3564
base_datos = (12345, 12345678, 98765, 85000, 3564)

inicio = input("Para comenzar precione solamente la tecla Enter  ") 
if inicio == '': #Si el usuario presiona unicamente la tecla ENTER se ejecuta el programa
    print("Ingrese su tarjeta  ")
    sleep(1.50)
    print("Validando su tarjeta...")
    sleep(1.50)
    clave_acceso = int(input("Ingrese su clave de acceso: ")) 
    intento = 0

    while clave_acceso != base_datos[0] and intento < 2: #Si la clave de acceso es erronea se solicita nuevamente. El máximo de intentos es 3
        clave_acceso = int(input("Ingrese su clave de acceso: "))
        intento = intento + 1

    if clave_acceso == base_datos[0]: #Si la clave de acceso es correcta se solicita el DNI
        dni = int(input("Ingrese su numero de DNI: "))
        if dni == base_datos[1]:
            print("Presione el numero de operación que desea realizar y luego la tecla ENTER")
            print("1. Consultas\n2. Retiros\n3. Transferencias\n4. Salir")
            seleccion = int(input("\n"))
            while seleccion != 4:
                if seleccion == 1:
                    sleep(1)
                    #FUNCION QUE HAGA CONSULTAS
                    print("1. Consultas\n2. Retiros\n3. Transferencias\n4. Salir")
                    seleccion = int(input("\n"))
                elif seleccion == 2:
                    sleep(1)
                    #FUNCION QUE HAGA RETIROS
                    print("1. Consultas\n2. Retiros\n3. Transferencias\n4. Salir")
                    seleccion = int(input("\n"))
                elif seleccion == 3:
                    sleep(1)
                    #FUNCION QUE HAGA TRANSFERENCIAS
                    print("1. Consultas\n2. Retiros\n3. Transferencias\n4. Salir")
                    seleccion = int(input("\n"))
            if seleccion == 4:
                print("Finalizando proceso...")
                sleep(1)
                exit
            else:
                print("Seleccion no valida")
                sleep(1)
                print("Finalizando proceso...")
                sleep(1)
                exit


    else: #Si la clave de acceso se ingresa mal 3 veces se sale del programa
        print("Ha ingresado su clave incorrectamente multiples veces")
        sleep(1)
        print("Finalizando proceso...")
        sleep(1)
        exit
else: #Si el usuario presiona otras teclas ademas de ENTER se sale del programa
    exit 
