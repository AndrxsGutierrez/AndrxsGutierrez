'''
12. Gimnasio: promedio de rendimiento semanal 
Registrar 5 personas en un gimnasio
Por cada una pedir: 
 nombre  
 días asistidos en la semana 
 minutos promedio entrenados por día 
Clasificar: 
 menos de 3 días → bajo compromiso 
 3 a 4 días → compromiso medio 
 5 o más → compromiso alto 
Al final mostrar cuántas personas quedaron en cada categoría. 
Practica: ciclos, contadores, condicionales.
'''
def days():
    while True:
        try:
            quantity = int(input('Enter the number of days: '))
            if quantity < 0:
                print('Invalid option, try again.')
            else:
                return quantity
        except ValueError:
            print('Invalid option, try again.')
def minutes():
    while True:
        try:
            quantity = int(input('Average minutes trained per day:'))
            if quantity < 0:
                print('Invalid option, try again.')
            else:
                return quantity
        except ValueError:
            print('Invalid option, try again.')
clients = {}
cont_low = 0
cont_med = 0
cont_higt = 0

for i in range (5):
    name = input("\nEnter the customer's name: ")
    con_days = days()
    con_minutes = minutes()
    clients[name] = []
    
    if con_days < 3:
        clients[name].append('Bajo compromiso')
        cont_low += 1

    elif con_days == 3 or con_days == 4:
        clients[name].append('Compromiso medio')
        cont_med += 1

    else:
        clients[name].append('Compromiso alto')
        cont_higt += 1
    
    print('Cliente regitrado con exito!')
    clients[name].append(f'Su promedio fue de {con_minutes} minutos diarios')
    clients[name].append(f'El cliente asistio {con_days} dias a la semana')


print (f'\nHubieron {cont_low} personas con bajo compromiso'
       f'\nHubieron {cont_med} personas con compromiso medio'
       f'\nHubieron {cont_higt} personas con compromiso alto'
       )

i = 0
print ('\n------CLIENTES-------')
for  nombre, datos in clients.items():
    i = i + 1
    print(f"{i} - {nombre} | {datos[0]} | {datos[1]} | {datos[2]}")
