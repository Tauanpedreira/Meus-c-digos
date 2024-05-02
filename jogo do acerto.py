import time
import random
print('\033[32molá, seja bem vindo!!')
time.sleep(2)
print('quero ver se você é bom ne jogos de acertos!!')
time.sleep(2)
sn=str(input('inciar o game ou esperar 1mn ?(S para iniciar, N para esperar 1mn): \033[m')).upper().strip()
pc=0
c=1
pc=random.randint(1,5)
if sn=='S':
    print('\033[32mok! vamos iniciar!!')
    time.sleep(2)
    player=int(input('pensei ne um número de 1 a 10... qual você acha que é? \033[m'))
    while not player==pc:
        if player !=pc:
            print('\033[32mhmmm...\033[m \033[31merrou, tente mais uma vez!!\033[m')
        c=c+1
        time.sleep(2)
        player=int(input('\033[32mqual você acha que é? \033[m'))
    if player==pc:
        if c<3:
            print('\033[33mnossa!! você é bom mesmo, apenas com {} vezes você já acertou!!\033[m'.format(c))
        elif c>3:
            print('\033[31mé... parabéns, mas deu pra perceber que você não tem muita sorte, você teve {} chances!!\033[31m'.format(c))
elif sn=='N':
    print('\033[32mblz, esperarei 1mn!!')
    time.sleep(60)
    print('OK! acabou o tempo!!\033[m')
    time.sleep(2)
    player=int(input('\033[32mpensei ne um número de 1 a 10... qual você acha que é? \033[m'))
    while not player==pc:
        print('\033[32mhmmm... \033[31merrou, tente mais uma vez!!\033[m')
        c=c+1
        time.sleep(2)
        player=int(input('\033[32mqual você acha que é? \033[m'))
    if player==pc:
        if c<3:
            print('\033[33mnossa!! você é bom mesmo, apenas com {} vezes você já acertou!!\033[m'.format(c))
        elif c>3:
            print('\033[31mé... parabéns, mas deu pra perceber que você não tem muita sorte, você teve {} chances!!\033[m'.format(c))
else:
    print('\033[31mpor favor, reinicie o programa e selecione uma das opções a cima!!\033[31m')
print('\033[31mFim de jogo.\033[m')
