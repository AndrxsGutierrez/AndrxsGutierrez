'''
#crear
with open('data/inventory.txt','w', newline="" ,encoding="utf-8") as file:
    writ = file.write('nada')

#lee
with open('data/inventory.txt','r', newline="" ,encoding="utf-8") as file:
    readed = file.read()
    print(readed)
'''
def data():
    name = input('Enter your name: ')
    last_name = input('Enter your last name: ')
    id = input('Enter your ID: ')
    country = input('what your from: ')
    return[name, last_name, id, country]

with open('data/name.txt','w', newline='',encoding='utf-8') as f:
    w = data()
    f.write(w)

with open('data/name.txt','r', newline='',encoding='utf-8') as f:
    read = f.read()
    print(read)
