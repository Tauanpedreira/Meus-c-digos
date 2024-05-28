import time
menor=0
maior=0
count=1
lista=list()
total=list()
print('olá, seja bem vindo!')
print('='*40)
while True:
    print('{}ª PESSOA'.format(len(total)+1).center(40,' '))
    print('='*40)
    lista.append(str(input('nome: ')))
    lista.append(int(input('idade: ')))
    total.append(lista[:])
    lista.clear()
    sn=str(input('quer continuar?(S/N): ')).upper().strip()[0]
    if sn=='S':
        print('='*40)
    elif sn=='N':
        print('encerrando programa...')
        time.sleep(2)
        print('='*40)
        break
for c in total:
    print('o nome da {} pessoa é {} e ela tem {} anos.'.format(count,c[0],c[1]))
    count+=1
    if c[1]<18:
        menor=+1
        print('essa pessoa é de MENOR!')
        print('='*40)
        time.sleep(1)
    elif c[1]>=18:
        maior=+1
        print('essa pessoa é de MAIOR!')
        print('='*40)
        time.sleep(1)
print('ao todo foram {} pessoas, {} de menor(es) e {} de maior(es).'.format(len(total),menor,maior))