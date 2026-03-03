#Nivel 4

def name():
    try:
        nombre = input("Ingrese su nombre: ")
        if nombre == "" or nombre == " " or nombre == "  " or nombre == "   " or nombre == "    " :
            print("el nombre no debe ser un espacio vacio")
            return name()
        elif nombre.isdigit():
            nombre = 5/0
        else:
            return nombre
    except ZeroDivisionError:
        print('El nombre no puede ser un numero')
        return name()

def cantidad():
    try:
        quantity = int(input("ingrese la cantidad: "))
        if quantity <=0:
            print("ingrese un numero mayor a 0")  
            return cantidad()
        else:
            return quantity
    except ValueError:
        print("Ingrese un numero.")
        return cantidad()
        
def namep():  
    nombre = input("Ingrese el nombre del producto: ")
    if nombre == "" or nombre == " ":
        print("El nombre del producto no debe ser un espacio vacio")
        return namep()
    else:
        return nombre
    
def price():
    try:
        quantity = int(input("Ingrese el precio del producto: "))
        if quantity <=0:
            print("ingrese un numero mayor a 0")
            return price()
        else:
            return quantity
    except ValueError:
        print("Ingrese un numero.")
        return price()
        
def client():  
    cliente = input("El cliente es Regular o VIP (R/V): ").lower()
    if cliente == "v" or cliente == "r":
        return cliente
    else:
        print('Opcion invalida, porfavor intente de nuevo.')
        return client()

    

Name_client = name()
Name_product = namep()
Price_product = price()
Quantity = cantidad()
TypeClient = client()
Subtotal = Price_product * Quantity

if Subtotal >= 50000 and TypeClient == "r":
    Total = (Subtotal*5)/100
    TotaL_Final = Subtotal - Total
    IVA = (TotaL_Final * 19) / 100
    TotalIVA = TotaL_Final + IVA
    print("\n ","\n ","RECIBO DE COMPRA","\n")
    print("Nombre del cliente:",Name_client)
    print("Producto comprado:",Name_product)
    print(f"Subtotal:{Subtotal:,.0f}")
    print(f"Descuento:{Total:,.0f}")
    print(f"Subtotal con descuento del 5%:{TotaL_Final:,.0f}")
    print(f"IVA 19%:{IVA:,.0f}")
    print(f"Total a pagar:{TotalIVA:,.0f}")

elif Subtotal >= 200000 and TypeClient == "v":
    Total = (Subtotal * 15) / 100
    TotaL_Final = Subtotal - Total
    IVA = (TotaL_Final * 19) / 100
    TotalIVA = TotaL_Final + IVA
    print("\n ","\n ","RECIBO DE COMPRA","\n")
    print("Nombre del cliente:",Name_client)
    print("Producto comprado:",Name_product)
    print(f"Subtotal:{Subtotal:,.0f}")
    print(f"Descuento:{Total:,.0f}")
    print(f"Subtotal con descuento del 15%:{TotaL_Final:,.0f}")
    print(f"IVA 19%:{IVA:,.0f}")
    print(f"Total a pagar:{TotalIVA:,.0f}")

elif Subtotal >= 50000 and TypeClient == "v":
    Total = (Subtotal * 10) / 100
    TotaL_Final = Subtotal - Total
    IVA = (TotaL_Final * 19) / 100
    TotalIVA = TotaL_Final + IVA
    print("\n ","\n ","RECIBO DE COMPRA","\n")
    print("Nombre del cliente:",Name_client)
    print("Producto comprado:",Name_product)
    print(f"Subtotal:{Subtotal:,.0f}")
    print(f"Descuento:{Total:,.0f}")
    print(f"Subtotal con descuento del 10%:{TotaL_Final:,.0f}")
    print(f"IVA 19%:{IVA:,.0f}")
    print(f"Total a pagar:{TotalIVA:,.0f}")

else:
    
    TotaL_Final = Subtotal
    IVA = (TotaL_Final * 19) / 100
    TotalIVA = TotaL_Final + IVA
    print("\n ","\n ","RECIBO DE COMPRA","\n")
    print("Nombre del cliente:",Name_client)
    print("Producto comprado:",Name_product)
    print(f"Subtotal:{Subtotal:,.0f}")
    print("Descuento: 0")
    print(f"Subtotal con descuento:{TotaL_Final:,.0f}")
    print(f"IVA 19%:{IVA:,.0f}")
    print(f"Total a pagar:{TotalIVA:,.0f}")

if TypeClient == 'v':
    TypeClient1 = 'VIP'
else:
    TypeClient1 = 'Regular'

print ('\nGracias por tu compra,',Name_client,'\nEres cliente',TypeClient1,'')

if TotalIVA <= 50000:
    print('Compra pequeña','\n ','\n ')
elif TotalIVA <= 150000:
    print('Compra mediana','\n ','\n ')
else:
    print('Compra grande','\n ','\n ')
    