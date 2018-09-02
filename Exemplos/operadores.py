n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
soma = n1 + n2
subtracao = n1 - n2
multiplicacao = n1 * n2
divisao = n1 / n2
potencia = n1 ** n2
divisaoInteira = n1 // n2
restoDaDivisao = n1 % n2

print('Soma {}, \nsubtracao {}, \nmultiplicacao {}, \ndivisao {:.3f}'.format(soma, subtracao, multiplicacao, divisao))
print('potencia {}, \ndivisao inteira {}, \nresto da divisao {}'.format(potencia, divisaoInteira, restoDaDivisao))
