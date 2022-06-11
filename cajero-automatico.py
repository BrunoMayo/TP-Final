from consultas import consultas

#clave = 12345
#dni = 12345678
#numero de cuenta = 98765
#saldo en ars = 85000
#saldo en soles = 3564
base_datos = [12345, 12345678, 98765, 85000, 3564]


inicio = input("Para comenzar precione solamente la tecla ENTER  ")
if inicio == '':
    print("Ingrese su tarjeta...")
    print("Validando tarjeta...")
    clave = int(input("Ingrese la clave de su tarjeta: "))
    if clave == base_datos[0]:
        dni = int(input("Ingrese su DNI: "))
        if dni == base_datos[1]:
            print("Presione:\n1.Para consultas\n2.Para Retiros\n3.Para transferencias\n4.Para Salir")
            opcion = int(input(""))
            while opcion != 4:
                if opcion == 1:
                    consultas(base_datos[3], base_datos[4])
                    print("Presione:\n1.Para consultas\n2.Para Retiros\n3.Para transferencias\n4.Para Salir")
                    opcion = int(input(""))
                elif opcion == 2:
                    print("Aca se hacen los retiros")
                    print("Presione:\n1.Para consultas\n2.Para Retiros\n3.Para transferencias\n4.Para Salir")
                    opcion = int(input(""))
                elif opcion == 3:
                    print("Aca se hacen las transferencias")
                    print("Presione:\n1.Para consultas\n2.Para Retiros\n3.Para transferencias\n4.Para Salir")
                    opcion = int(input(""))
                else:
                    print("Presione:\n1.Para consultas\n2.Para Retiros\n3.Para transferencias\n4.Para Salir")
                    opcion = int(input(""))
        else:
            print("El DNI ingresado es incorrecto")    
else:
    print("La clave ingresada no es valida")
