# FORMATAÇÃO DE STRING, VAMOS VER F STRING

nome = 'Karlison Matos'
altura = 1.63
peso = 65
imc = peso / (altura * altura)

# f-strings (é o f antes da string na variavel)
linha_1 = f'{nome} tem {altura:.2f} de altura'
linha_2 = f'pesa {peso} quilos e seu IMC é'
linha_3 = f'{imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)

# Karlison Matos te, 1.63 de altura,
# pesa 6 quilos e seu IMC é
# IMC 