import time
c=0
sn=str(input('\033[34molá, vamos jogar jokenpô?(S/N): ')).strip().lower()[0]
if sn=='s':
    print('vamos lá!!\033[m')
    time.sleep(2)
    while True:
        ppt='ola pedra papel tesoura'
        from random import randint
        separado=ppt.split()
        pc=randint(1,3)
        print('\033[34mescolha qual você vai jogar:')
        print('[1] pedra')
        print('[2] papel')
        print('[3] tesoura\033[m')
        player=int(input('\033[34mqual você vai jogar? \033[m'))
        print('\033[34meu escolhi {} e você {}\033[m'.format(separado[pc],separado[player]))
        if player==1 and pc==2:
            print('\033[31mGANHEI!! HAHAHA!!\033[m')
            break
        elif player==2 and pc==1:
            print('\033[32mparabéns!! você venceu!!\033[m')
            c+=1
        elif player==3 and pc==1:
            print('\033[31mGANHEI!! HAHAHA!!\033[m')
            break
        elif player==1 and pc==3:
            print('\033[32mparabéns!! você venceu!!\033[m')
            c+=1
        elif player==2 and pc==3:
            print('\033[31mGANHEI!! HAHAHA!!\033[m')
            break
        elif player==3 and pc==2:
            print('\033[32mparabéns você venceu!!\033[m')
            c+=1
        else:
            print('\033[33mEmpate.\033[m')
    if c>0:
        print('\033[32mvocê teve o total de {} vitórias!!\033[m'.format(c))
    elif c==0:
        print('\033[31mnão ganhou nenhuma >:)\033[m')
elif sn=='n':
    print('\033[31mpoxa... que pena :(\033[m')
print('\033[31mFim\033[m')
