import time
import random
from uteis.interfase import deco
print('\033[32molá, seja bem vindo.\033[m')
time.sleep(0.5)
print('\033[33mchecando arquivo de histórico...\033[m')
time.sleep(1)
very=deco.very('historico.txt')
time.sleep(1)
while True:
    if very==False:
        break
    deco.menu('\033[34mMENU DO JOGO\033[m')
    print('\033[34m[1] começar o jogo.')
    print('[2] Histórico de Partidas.')
    print('[3] sair do jogo.\033[m')
    op=deco.op()
    if op==3:
        print('\033[34msaindo... até logo :)\033[m')
        break
    else:
        if op==2:
            deco.menu('\033[34mHISTÓRICO DE PARTIDAS\033[m')
            a=open('historico.txt','rt')
            print(a.read())
            while True:
                try:
                    sn=str(input('\033[34mescreva VOLTAR pra voltar: \033[m')).upper().strip()
                    if sn=='VOLTAR':
                        break
                    else:
                        print('\033[31mpor favor escreva VOLTAR.\033[m')
                except:
                    print('\033[31mERRO: ocorreu um ERRO inesperado.\033[m')
                    break
        if op==1:
            print('\033[34mcomeçando...\033[m')
            chance=3
            time.sleep(2)
            while True:
                try:
                    if chance==0:
                        break
                    elif chance!=0:
                        chance=3
                    ok=str(input('\033[32mPC: olá, eu sou o seu computador, iremos jogar um mini-game de adivinhação ok? \033[m')).upper().strip()
                    if 'OK' in ok:
                        print('\033[32mVAMOS LÁ!!\033[m')
                        time.sleep(2)
                        computador=random.randint(1,11)
                        print('\033[32mPC: acabei de pensar em um número... tente adivinhar de 0 a 10!\033[m')
                        time.sleep(1)
                        while True:
                            try:
                                player=int(input('\033[34mhmm.. qual número você acha que o PC pensou? \033[m'))
                                if player==computador:
                                    print('\033[32mPC: parabéns!! você acertou!!\033[m')
                                    a=open('historico.txt','at')
                                    a.write('\033[32mquantidade de vidas: {}\033[m\n'.format(chance))
                                    a.close()
                                    break
                                elif player!=computador:
                                    chance=chance-1
                                    if chance>0:
                                        print('\033[32mPC: ... tente novamente você só tem mais {} chances!!\033[m'.format(chance))
                                    if chance==0:
                                        print('\033[31mPC: GAME OVER\033[m')
                                        a=open('historico.txt','at')
                                        a.write('\033[31mGAME OVER\033[m\n')
                                        a.close()
                                        break
                            except:
                                print('\033[31mERRO: tente com um número de 0 a 10!!\033[m')

                    else:
                        print('\033[32mPC: ...\033[m')
                except:
                    print('\033[31mERRO: ocorreu um ERRO inesperado.\033[m')
                    break