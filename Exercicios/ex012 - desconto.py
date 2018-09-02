valor = float(input('Digite o valor do produto: '))
desconto = valor / 100 * 5
valorDesconto = valor - desconto
print('Valor antigo {}R$\nDesconto de 5%: {}R$'.format(valor, valorDesconto))

