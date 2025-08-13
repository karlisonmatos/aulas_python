# if / elif / else
# se / se não se / se não

entrada = input('Você quer "entrar" ou "sair"? ')

if entrada == 'entrar':
    print('Você entrou no sistema') # o tab abaixo da condição indica que aquele print é daquele if
elif entrada == 'sair':
    print('Você saiu do sistema')
else:
    print('Você não digitou nem entrar e nem sair.')


# a sintaxe acima analisa a digitação da str considerando letra maiuscula e minuscula