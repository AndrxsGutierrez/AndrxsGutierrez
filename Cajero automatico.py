Inicial_Balance = 1000

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
        if Number <=0:
            print("ingrese un numero mayor a 0")  
            return operations()
        else:
            return Number
    except ValueError:
        print("Ingrese un numero.")
        return operations()
    
def RetMoney():
    try:
        quantity = int(input("Cuantas operaciones desea realizar: "))
        if quantity <=0:
            print("ingrese un numero mayor a 0")  
            return RetMoney()
        else:
            return quantity
    except ValueError:
        print("Ingrese un numero.")
        return RetMoney()

def DepMoney():
    try:
        quantity = int(input("Cuantas operaciones desea realizar: "))
        if quantity <=0:
            print("ingrese un numero mayor a 0")  
            return DepMoney()
        else:
            return quantity
    except ValueError:
        print("Ingrese un numero.")
        return DepMoney()

while operations() != 0:
    