cotacao = float(3.27)
carteira = float(input('Quanto tem na carteira? '))
qtdDolar = carteira / cotacao
print('Voce tem {} reais e pode comprar {:.2f} dolares\n'
      'Cotação atual {}'.format(carteira, qtdDolar, cotacao))
