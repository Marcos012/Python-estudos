qtdMetros = float(input('Entre com um valor em metros: '))
cm = qtdMetros*(10**2)
mm = qtdMetros*(10**3)
km = qtdMetros/(10**3)

print('Valor em metros: {}\nCm: {}\nMM: {}\nKm: {}'.format(qtdMetros, cm, mm, km))
