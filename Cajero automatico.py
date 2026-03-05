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

def Userde():
    try:
        quantity = int(input('Ingresa tu numero de usuario: '))
        if quantity <=0:
            print("ingrese un numero mayor a 0")  
            return operations()
        else:
            return quantity
    except ValueError:
        print("Ingrese un numero.")
        return operations()

def Clavede():
    try:
        quantity = int(input('Ingresa tu clave: '))
        if quantity <=0:
            print("ingrese un numero mayor a 0")  
            return operations()
        else:
            return quantity
    except ValueError:
        print("Ingrese un numero.")
        return operations()


Usuario = 1234
clave = 2122
Inicial_Balance = 1000
contador = 0

print ('\n','Solo tienes 4 intentos')
while contador < 4:
    
    Usuarioped = Userde()
    claveoped  = Clavede()
    if Usuarioped == Usuario and claveoped == clave:
        print('\n','Usted ha ingresado correctamente.','\n')
        break
        
    elif Usuarioped != Usuario or claveoped != clave:
        print('\n','Acceso denegado, intente nuevamente.','\n')
        contador += 1
if contador == 4:
    print('\n','Haz hecho demasiados intentos','\n')
    exit()

    

operation = operations()

for I in range (operation):

    print('     RiwiBank      ')
    print('-------MENU-------')
    print('1 - Consultar saldo')
    print('2 - Retirar dinero')
    print('3 - Depositar dinero')
    print('4 - Salir')
    print('-------------------','\n')


    opcion_Num = opcion()
    montoactual = RetMoney()
    
    if opcion_Num == 1:
        print('\n','Su saldo actual es de',Inicial_Balance,'\n')

    elif opcion_Num == 2:
        Inicial_Balance -= montoactual
        print ('\n','Usted ha retirado',montoactual)
        print ('Su saldo actual es de',Inicial_Balance,'\n')

    elif opcion_Num == 3:
        montoactual = DepMoney()
        Inicial_Balance += montoactual
        print ('\n','Usted ha depositado',montoactual)
        print ('Su saldo actual es de',Inicial_Balance,'\n')
    
    else:
        print(' ')
        break

print ('Gracias por usar nuestro cajero automatico!','\n')

    
    
    
        
        
            


   






    