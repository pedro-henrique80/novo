n = input('digite algo: ')

print('qual o tipo disso?', type(n))
print('isso possui apenas espaços?', n.isspace())
print('isso é um número?', n.isnumeric())
print('isso é alfabético?', n.isalpha())
print('isso é alfanúmerico?', n.isalnum())
print('isso é um decimal?', n.isdecimal())