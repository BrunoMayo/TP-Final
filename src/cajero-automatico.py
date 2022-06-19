from consultas import consultas, saldo_o_movimientos, soles_o_pesos, escribir_o_imprimir
from retiros import cuenta_a_debitar, retiros
from transferencias import transferir, monto_a_operar

#clave = 12345
#dni = 12345678
#numero de cuenta = 98765
#saldo en ars = 85000
#saldo en soles = 3564
base_datos = [12345, 12345678, 98765, 85000, 3564] #Datos provistos en el PDF con los enunciados


inicio = input("Para comenzar precione solamente la tecla ENTER  ") #Se solicita al usuario que ingrese enter para que el cajero comienze a funcionar
if inicio == '': #Si se presiona unicamente enter
    try:
        print("Ingrese su tarjeta...")
        print("Validando tarjeta...")
        clave = int(input("Ingrese la clave de su tarjeta: ")) #Se solicita la clave de la tarjeta
        if clave == base_datos[0]: #Si la clave es correcta
            dni = int(input("Ingrese su DNI: ")) #Se solicita el DNI
            if dni == base_datos[1]: #Si el DNI es correcto
                print("Presione:\n1.Para consultas\n2.Para retiros\n3.Para transferencias\n4.Para salir\n5.Pasar 3 dias\n") #Se da a elegir la operaciona realizar
                opcion = int(input(""))
                monto_a_devolver_pesos = 0 #Aca se almacena el dinero a devolver en caso de que la cuenta a la que se quiere transferir sea erronea
                monto_a_devolver_soles = 0 #Aca se almacena el dinero a devolver en caso de que la cuenta a la que se quiere transferir sea erronea
                while opcion != 4: #Mientras no se elija la opcion salir
                    if opcion == 1: #Si se elije la opcion 1
                        try:
                            moneda = soles_o_pesos() #Se da a elegir la moneda a utilizar
                            opcion_escribir_o_imprimir = escribir_o_imprimir() #Se da a elegir si se desea imprimir la consulta por pantalla o si se prefiere imrpimir un ticket
                            opcion_saldo_o_movimientos = saldo_o_movimientos() #Se da a elegir que operacion se desea consultar, si el saldo o los ultimos movimientos
                            consultas(base_datos[3], base_datos[4], opcion_saldo_o_movimientos, moneda, opcion_escribir_o_imprimir) #Se llama a la funcion que permite hacer consultas
                        except ValueError as exc: #En caso de que se ingrese un valor con un tipo de dato no permitido
                            print("Debe completar con datos validos.") #Se da aviso
                        print("Presione:\n1.Para consultas\n2.Para retiros\n3.Para transferencias\n4.Para salir\n5.Pasar 3 dias\n") #Se vuelve a dar a elegir una operacion
                        opcion = int(input(""))
                    elif opcion == 2: #Si se elige la operacion 2
                        try:
                            cuenta_donde_debitar = cuenta_a_debitar() #Se da a elegir la cuenta de la que se debitara
                            moneda = soles_o_pesos() #Se da a elegir la moneda a utilizar
                            monto = monto_a_operar(base_datos[3], base_datos[4], moneda) #se solicita el monto a realizar
                            imprimir = input("Presione 1 y luego ENTER si desea imprimir voucher comprobante de retiro: ") #Se da la opcion de imprimir un voucher con el returo
                            saldos_retiros = retiros(base_datos[3], base_datos[4], moneda, cuenta_donde_debitar, monto, imprimir) #Se llama a la funcion que hace los retiros de dinero
                            base_datos[3] = saldos_retiros[0] #Se acutaliza el monto en pesos despues del retiro
                            base_datos[4] = saldos_retiros[1] #Se actualiza el monto en soles despues del retiro
                        except ValueError as exc: #En caso de que se ingrese un valor con un tipo de dato no permitido
                            print("Debe completar con datos validos.") #Se da aviso
                        print("Presione:\n1.Para consultas\n2.Para retiros\n3.Para transferencias\n4.Para salir\n5.Pasar 3 dias\n") #Se vuelve a dar a elegir una operacion
                        opcion = int(input(""))
                    elif opcion == 3: #Si se elige la operacion 3
                        try:
                            moneda = soles_o_pesos() #Se da aelegir la moneda a utilizar
                            monto = monto_a_operar(base_datos[3], base_datos[4], moneda) #se solicita el monto a realizar
                            cuenta = int(input("Ingrese el numero de cuenta al que le desea transferir: ")) #Se solicita el numero de cuenta a transferir
                            saldos_transferencia = transferir(base_datos[2], base_datos[3], base_datos[4], moneda, monto, cuenta) #Se llama a la funcion que realiza las transferencias
                            base_datos[3] = saldos_transferencia[0] #Se actualiza el monto en pesos despues de transferir
                            base_datos[4] = saldos_transferencia[1] #Se actualiza el monto en soles despues de transferir
                            if not saldos_transferencia[2]: #Si la cuenta a la que se quiso transferir no existe
                                monto_a_devolver_pesos = monto_a_devolver_pesos + saldos_transferencia[3] #Se almacena el monto que se debera devolver despues de 3 dias
                                monto_a_devolver_soles = monto_a_devolver_soles + saldos_transferencia[4] #Se almacena el monto que se debera devolver despues de 3 dias
                        except ValueError as exc: #En caso de que se ingrese un valor con un tipo de dato no permitido
                            print("Debe completar con datos validos.") #Se da aviso
                        print("Presione:\n1.Para consultas\n2.Para retiros\n3.Para transferencias\n4.Para salir\n5.Pasar 3 dias\n") #Se vuelve a dar a elegir una operacion
                        opcion = int(input(""))
                    elif opcion == 5: #Si se elige la opcion 5, se simula el paso de 3 dias
                        base_datos[3] = base_datos[3] + monto_a_devolver_pesos #Se devuelve el acumulado de montos a devolver
                        base_datos[4] = base_datos[4] + monto_a_devolver_soles #Se devuelve el acumulado de montos a devolver
                        print("Presione:\n1.Para consultas\n2.Para retiros\n3.Para transferencias\n4.Para salir\n5.Pasar 3 dias\n") #Se vuelve a dar a elegir una operacion
                        opcion = int(input(""))
                    else: #Si se preciona una opcion que no existe se vuelve a dar a elegir
                        print("Presione:\n1.Para consultas\n2.Para retiros\n3.Para transferencias\n4.Para salir\n5.Pasar 3 dias\n") #Se vuelve a dar a elegir una operacion
                        opcion = int(input(""))
            else:
                print("El DNI ingresado es incorrecto")    
        else:
            print("La clave ingresada no es valida")
    except ValueError as exc:
        print("Debe completar con datos validos.") #Se da aviso de que los valores ingresados no son del tipo correcto