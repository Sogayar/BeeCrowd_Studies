'''Leia um valor inteiro entre 1 e 12, inclusive. Correspondente a este valor, deve ser apresentado como resposta o mês do ano por extenso, em inglês, com a primeira letra maiúscula.

Entrada
A entrada contém um único valor inteiro.

Saída
Imprima por extenso o nome do mês correspondente ao número existente na entrada, com a primeira letra em maiúscula.'''

n_month = int(input())
month = ['January', 'February', 'March', 'April', 'May', 'June', 'July','August', 'September', 'October', 'November', 'December']
print(month[n_month - 1])

'''
# MANEIRA MANEIRA NADA BOA DE SE FAZER
num = int(input())
if num == 1:
    print('January')
elif num == 2:
    print('February')
elif num == 3:
    print('March')
elif num == 4:
    print('April')
elif num == 5:
    print('May')
elif num == 6:
    print('June')
elif num == 7:
    print('July')
elif num == 8:
    print('August')
elif num == 9:
    print('September')
elif num == 10:
    print('October')
elif num == 11:
    print('November')
elif num == 12:
    print('December')'''
    
