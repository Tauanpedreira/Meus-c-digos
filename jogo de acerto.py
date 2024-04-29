import time
import random
pergunta=str(input('\033[34molá! pronto para iniciar um game divertido comigo ou quer 1 mn?(S/N): \033[m').upper())
if pergunta=='S':
    print('\033[34mok! vamos iniciar!!\033[m')
    time.sleep(1)
    print('\033[34mpensei ne um número de 0 a 5... tente adivinhar!!\033[m')
    num=random.randint(0,5)
    player=int(input('qual número você acha que o computador pensou? '))
    if player==num:
        print('\033[32mPARABENS!! você venceu!!!\033[m')
    else:
        print('\033[31mque pena... esperava mais de você!\033[m')
if pergunta=='N':
    print('\033[32mok! te darei 1 minuto! se aprece!!\033[m')
    time.sleep(60)
    print('\033[31mok! acabou o seu tempo, vamos iniciar!!\033[m')
    time.sleep(1)
    print('\033[34mpensei ne um número de 0 a 5... tente adivinhar!!\033[m')
    num2=(random.randint(0,5))
    player2=int(input('qual número você acha que o computador pensou? '))
    if player2==num2:
        print('\033[32mPARABENS!! você venceu!!!\033[m')
    else:
        print('\033[31mque pena... esperava mais de você!\033[m')
print('\033[31mFim de jogo.\033[m')
