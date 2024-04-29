import time
print('olá, seja bem-vindo!!')
time.sleep(1)
num=int(input('qual número você quer ver a tabuada? '))
for t in range(1,11):
    print('{}x{}={}'.format(num,t,num*t))
    time.sleep(1)
print('espero ter ajudado!! :)')