l = float(input('digite a largura da parede: '))
h = float(input('digite a altura da parede: '))

A = l * h
T = A / 2

print('A sua parede de {}m² necessita de {:.2f}L de tinta para ser pintada' .format(A, T))