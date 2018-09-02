altura = float(input('Altura da parede: '))
largura = float(input('Largura da parede: '))
area = altura * largura

qtdTinta = area / 2

print('\nA área da parede é {}\n'
      'Necessário {}L de tinta para pintar'.format(area, qtdTinta))
