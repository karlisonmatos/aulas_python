# Operadores in e not in
# Strings em python são iteraveis, elas seguem um indice
# 0 1 2 3 4 5 6 7
# K a r l i s o n

nome = 'Karlison'
print(nome[2])

# o código acima está imprimindo o indice [2], a letra r do nome

print('g' in nome)

# o código acima confirma, g está em nome, no caso não e ele retorna false
# not in, faz a mesma lógica, perguntando ao contrario (não está)

variavel_a = 1 or 0
variavel_b = 0 or 1
print(variavel_a, variavel_b)


# código abaixo é de um quiz da aula
numero = 10
if numero > 1:
    if numero >2:
        if numero > 3:
            print('Numero maior que 3')
        else:
            print('Numero menor que 3')
    else:
        print('Numero menor que 2')
else:
    print('Numero menor que 1')