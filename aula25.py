# INTERPOLAÇÃO BÁSICA DE STRINGS
# s - string
# d e i - int
# f - float
# x e X - hexadecimal

nome = 'Karlison'
preco = 1000.959493093
variavel = '%s, o preço total é R$ %2.f' % (nome, preco)
print(variavel)

# na interpolação, a %s puxa a string que é o nome, e o %f puxa o preco que é um int

print('O hexadecimal de %d é %04x' % (1500, 1500))

# no código acima é um exemplo de transformar em hexadecimal
# %04 significa a quantidade casas decimais