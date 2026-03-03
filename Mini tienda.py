#Nivel 4
def name():
    nombre = input("Ingrese su nombre: ")
    if nombre == "" or nombre == " ":
        print("el nombre no debe ser un espacio vacio")
        return name()
    else:
        return nombre

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
        
Name_client = name()
Name_product = namep()
Price_product = price()
Quantity = cantidad()
TypeClient = input("El cliente es Regular o VIP (R/V): ").lower()
Subtotal = Price_product * Quantity

if Subtotal >= 50000 and TypeClient == "r":
    Total = (Subtotal*5)/100
    TotaL_Final = Subtotal - Total
    IVA = (TotaL_Final * 19) / 100
    TotalIVA = TotaL_Final + IVA
    print("\n ","\n ","RECIBO DE COMPRA","\n")
    print("Nombre del cliente:",Name_client)
    print("Producto comprado:",Name_product)
    print("Subtotal:",Subtotal)
    print("Descuento:",Total)
    print("Subtotal con descuento del 5%:",TotaL_Final)
    print("IVA 19%:",IVA)
    print("Total a pagar:",TotalIVA)

elif Subtotal >= 200000 and TypeClient == "v":
    Total = (Subtotal * 15) / 100
    TotaL_Final = Subtotal - Total
    IVA = (TotaL_Final * 19) / 100
    TotalIVA = TotaL_Final + IVA
    print("\n ","\n ","RECIBO DE COMPRA","\n")
    print("Nombre del cliente:",Name_client)
    print("Producto comprado:",Name_product)
    print("Subtotal:",Subtotal)
    print("Descuento:",Total)
    print("Subtotal con descuento del 15%:",TotaL_Final)
    print("IVA 19%:",IVA)
    print("Total a pagar:",TotalIVA)

elif Subtotal >= 50000 and TypeClient == "v":
    Total = (Subtotal * 10) / 100
    TotaL_Final = Subtotal - Total
    IVA = (TotaL_Final * 19) / 100
    TotalIVA = TotaL_Final + IVA
    print("\n ","\n ","RECIBO DE COMPRA","\n")
    print("Nombre del cliente:",Name_client)
    print("Producto comprado:",Name_product)
    print("Subtotal:",Subtotal)
    print("Descuento:",Total)
    print("Subtotal con descuento del 10%:",TotaL_Final)
    print("IVA 19%:",IVA)
    print("Total a pagar:",TotalIVA)

else:
    
    TotaL_Final = Subtotal
    IVA = (TotaL_Final * 19) / 100
    TotalIVA = TotaL_Final + IVA
    print("\n ","\n ","RECIBO DE COMPRA","\n")
    print("Nombre del cliente:",Name_client)
    print("Producto comprado:",Name_product)
    print("Subtotal:",Subtotal)
    print("Descuento: 0")
    print("Subtotal con descuento:",TotaL_Final)
    print("IVA 19%:",IVA)
    print("Total a pagar:",TotalIVA)

