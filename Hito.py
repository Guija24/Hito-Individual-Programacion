
print('-------------------------------------------')
print('   Bienvenidos al Concesionario de Cohes   ')
print('-------------------------------------------')
print()
print()

print('   Menu Principal   ')
print('--------------------')
Menu=int(input("\n 1-REGISTRARSE \n 2-SELECCIONAR COCHE \n 3-PAGAR \n 4-CODIGO DE SEGUIMIENTO \n 5-SALIR \n ->  "))
while Menu!=0:
    if Menu==1:
        print()
        print('   Registro   ')
        print('--------------')
        Nombre=input('Nombre: ')
        Apellidos:input('Apellidos: ')
        dni=input('DNI: ')
        Tlf=input('Telf: ')
        Correo=input('Correo Electronico: ')
    elif Menu==2:
        print()
        print('   Elige el coche   ')
        print('--------------------')
        print()
        print('1-NissanGTR')
        print('2-Audi R8 V10')
        print('3-Subaru Impreza STI')
        print('4-Volskvaguen Golf GTI')
        print('5-Range Rover Velar')
        MenuC=int(input('Que coche quieres comprar Nº: '))
        if MenuC==1:
            print()
            print('Has elegido el NissanGTR')
        elif MenuC==2:
            print()
            print('Has elegido el Audi R8 V10')
        elif MenuC==3:
            print()
            print('Has elegido el Subaru Impreza STI')
        elif MenuC==4:
            print()
            print('Has elegido el Volskvaguen Golf GTI')
        elif MenuC==5:
            print()
            print('Has elegido el Range Rover Velar')
        else:
            print()
            print('Ese coche no esta')
    elif Menu==3:
        print()
        print('   Efectuar Pago   ')
        print('-------------------') 
        NTarjeta=input('Nª Tarjeta: ')
        FValidez=input('Valida Hasta: ')
        cvv=input('CVV: ')
        print()
        print(f'-----La factura se enviara al siguiente correo: {Correo} -----')
    elif Menu==4:
        print(f'Su codigo de seguimiento se le enviara al {Tlf} y a {Correo}')
    elif Menu==5:
        break
    else:
        print()
        print('Esa eleccion no existe')

    print()
    print('   Menu Principal   ')
    print('--------------------')
    Menu=int(input("\n 1-REGISTRARSE \n 2-SELECCIONAR COCHE \n 3-PAGAR \n 4-CODIGO DE SEGUIMIENTO \n 5-SALIR \n ->  "))