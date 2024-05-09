print('{:=^40}'.format(' loja super barata!! '))
c=0
s=0
while True:
    produto=str(input('digite o nome do produto: '))
    preco=float(input('digite o valor do produto: '))
    desconto=int(input('digite o desconto: '))
    tolt=(desconto*preco)/100
    tolta=preco-tolt
    print('o produto passa a ter o valor de {:.2f} R$ com menos {}% para pagar ({:.2f} R$)!!'.format(tolta,desconto,tolt))
    break