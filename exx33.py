n1 = int(input('digite um número: '))
n2 = int(input('digite outro número: '))
n3 = int(input('digite mais um número: '))

#maior?
if n1 > n2 and n1 > n3:
    maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n2:
    maior = n3
print(f'maior = {maior}')
#menor?
if n1 < n2 and n1 < n3:
    menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n2 and n3 < n1:
    menor = n3
print(f'menor = {menor}')