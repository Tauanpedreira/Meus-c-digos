import time
import random
pergunta=str(input('olá! pronto para iniciar um game divertido comigo ou quer 1 mn?(S/N): ').upper())
if pergunta=='S':
    print('ok! vamos iniciar!!')
    time.sleep(1)
    print('pensei ne um número de 0 a 5... tente adivinhar!!')
    num=random.randint(0,5)
    player=int(input('qual número você acha que o computador pensou? '))
    if player==num:
        print('\033[32mPARABENS!! você venceu!!!\033[m')
    else:
        print('\033[31mque pena... esperava mais de você!\033[m')
if pergunta=='N':
    print('ok! te darei 1 minuto! se aprece!!')
    time.sleep(60)
    print('ok! acabou o seu tempo, vamos iniciar!!')
    time.sleep(1)
    print('pensei ne um número de 0 a 5... tente adivinhar!!')
    num2=(random.randint(0,5))
    player2=int(input('qual número você acha que o computador pensou? '))
    if player2==num2:
        print('\033[32mPARABENS!! você venceu!!!\033[m')
    else:
        print('\033[31mque pena... esperava mais de você!\033[m')
print('\033[31mFim de jogo.\033[m')