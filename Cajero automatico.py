Inicial_Balance = 1000
Pin = 2478
contador = 0

def operations():
    try:
        quantity = int(input("Cuantas operaciones desea realizar: "))
        if quantity <=0:
            print("ingrese un numero mayor a 0")  
            return operations()
        else:
            return quantity
    except ValueError:
        print("Ingrese un numero.")
        return operations()
    
def opcion():
    try:
        Number = int(input("Eliga una opcion: "))
        if Number <=0 or Number > 4:
            print("Opcion invalida, intente nuevamente.")  
            return opcion()
        else:
            return Number
    except ValueError:
        print("Opcion invalida, intente nuevamente.")
        return opcion()
    
def RetMoney():
        try:
            monto = int(input('Ingrese el monto a retirar: '))
            if monto > Inicial_Balance:
                print ('Fondos insuficientes')
                return RetMoney()
            elif monto <= 0:
                print ('no puedes ingresar un monto negativo')
                return RetMoney()
            else:
                return monto
        except ValueError:
            print ('No puedes ingresar letras, intente nuevamente')
            return RetMoney() 
        
def DepMoney():
        try:
            monto = int(input('Ingrese el monto a depositar: '))
            if monto <= 0:
                print ('no puedes depositar un monto negativo')
                return DepMoney()
            else:
                return monto
        except ValueError:
            print ('No puedes ingresar letras, intente nuevamente')
            return DepMoney() 

while co
    pin = int(input('Ingrese su pin para poder acceder al menu: '))
    if pin == Pin:
        print ('Acceso permitido')

    if pin != Pin:
        print ('haz errado, te quedan 3 intentos')
        if pin != Pin:
            print ('haz errado, te quedan 2 intentos')
            if pin != Pin:
                print ('haz errado, te quedan 1 intentos')
                if pin != Pin:
                    print ('haz errado, te quedan 0 intentos')
                    break
        
    

    operation = operations()

    for I in range (operation):

        print('     RiwiBank      ')
        print('-------MENU-------')
        print('1 - Consultar saldo')
        print('2 - Retirar dinero')
        print('3 - Depositar dinero')
        print('4 - Salir')

        opcion_Num = opcion()
        
        if opcion_Num == 1:
            print('\n','Su saldo actual es de',Inicial_Balance,'\n')

        elif opcion_Num == 2:
            montoactual = RetMoney()
            Inicial_Balance -= montoactual
            print ('\n','Usted ha retirado',montoactual)
            print ('Su saldo actual es de',Inicial_Balance,'\n')

        elif opcion_Num == 3:
            montoactual = DepMoney()
            Inicial_Balance += montoactual
            print ('\n','Usted ha depositado',montoactual)
            print ('Su saldo actual es de',Inicial_Balance,'\n')
        
        else:
            break
    
    print ('Gracias por usar nuestro cajero automatico')

    
    
    
        
        
            


   






    