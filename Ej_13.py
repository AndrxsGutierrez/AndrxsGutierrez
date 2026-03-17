menu = ['1 - Cafe $4000', '2 - Capuchino $7000', '3 - Pastel $6000']
café = 4000 
capuchino = 7000 
pastel = 6000 
vendido = []
def opcion():
    while True:
        try:
            esc = int(input('Escoja el producto a escoger: '))
            if esc <= 0 or esc > 3:
                print ('Invalid option, try again.')
            else:
                return esc
        except ValueError:
            print ('Invalid option, try again.')
def quantity():
    while True:
        try:
            es = int(input('Cantidad del producto: '))
            if es <= 0:
                print ('Invalid option, try again.')
            else:
                return es
        except ValueError:
            print ('Invalid option, try again.')
def opcion_seg():
    while True:
        try:
            esc = int(input('Quieres registrar un cliente marca (1) si quieres salir marca (2): '))
            if esc <= 0 or esc > 2:
                print ('Invalid option, try again.')
            else:
                return esc
        except ValueError:
            print ('Invalid option, try again.')

while True: 
    seguir = opcion_seg()
    if seguir == 2:
        break
    
    name_client = input('Ingrese el nombre del cliente: ')
    for i in menu:
        print(i)
    Opcion = opcion()
    Quantity = quantity()

    match Opcion:
        case 1:
            total = café * Quantity
        case 2:
            total = capuchino * Quantity
        case 3:
            total = pastel * Quantity
    
    if total > 20000:
        descuento = total * 0.1
        total -= descuento
        print ('El descuento es de:',descuento,'\nTotal con descuento:',total)
    else:
        print ('Total:',total)
    vendido.append(total)

print (f'Total vendido fue de {sum(vendido)}')
print ('\nPrograma finalizado.')