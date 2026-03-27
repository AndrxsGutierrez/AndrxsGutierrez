import csv
print('Welcome to coders RIWI')
'''
coder = input("what's your name: ")
city = input("what's your from: ")
clan = input("what's your clan: ")

with open('data/coders.csv','w',newline='',encoding='utf-8') as f:
    writer = csv.DictWriter(f,fieldnames=['coder','city','clan'])
    writer.writeheader()
    writer.writerow({'coder':coder,'city':city,'clan':clan})
'''
while True:
    op = input('Quieres agregar un coder a coders.csv? SI/NO (S/N): ').lower()
    if op == 'n':
        print('bye')
        break
    coder = input("what's your name: ")
    city = input("what's your from: ")
    clan = input("what's your clan: ")
    with open('data/coders.csv','a',newline='',encoding='utf-8') as f:
        writer = csv.DictWriter(f,fieldnames=['coder','city','clan'])
        writer.writerow({'coder':coder,'city':city,'clan':clan})

with open('data/coders.csv','r',newline='',encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for read in reader:
            print(read)



