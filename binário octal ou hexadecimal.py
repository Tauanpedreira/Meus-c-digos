num=int(input('digite um número: '))
print('escolha uma opção')
print('[1] binário')
print('[2] octal')
print('[3] hexadecimal')
opçao=int(input('sua opção: '))
if opçao==1:
    print('o número {} em binário é {}'.format(num,bin(num)))
elif opçao==2:
    print('o número {} em octal é {}'.format(num,oct(num)))
elif opçao==3:
    print('o número {} em hexadecimal é {}'.format(num,hex(num)))
else:
    print('\033[31mpor favor, tente novamente com uma opção valida!!\033[m')