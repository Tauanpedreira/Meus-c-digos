import time
sn=str(input('olá, vamos jogar jokenpô?(S/N): ')).strip().lower()
if sn=='s':
    print('vamos lá!!')
    time.sleep(2)
    ppt='ola pedra papel tesoura'
    from random import randint
    separado=ppt.split()
    pc=randint(1,3)
    print('escolha qual você vai jogar:')
    print('[1] pedra')
    print('[2] papel')
    print('[3] tesoura')
    player=int(input('qual você vai jogar? '))
    print('eu escolhi {} e você {}'.format(separado[pc],separado[player]))
    if player==1 and pc==2:
        print('\033[31mGANHEI!! HAHAHA!!\033[m')
    elif player==2 and pc==1:
        print('\033[32mparabéns!! você venceu!!\033[m')
    elif player==3 and pc==1:
        print('\033[31mGANHEI!! HAHAHA!!\033[m')
    elif player==1 and pc==3:
        print('\033[32mparabéns!! você venceu!!\033[m')
    elif player==2 and pc==3:
        print('\033[31mGANHEI!! HAHAHA!!\033[m')
    elif player==3 and pc==2:
        print('\033[32mparabéns você venceu!!\033[m')
    else:
        print('\033[33mEmpate.\033[m')
print('\033[32mFim\033[m')