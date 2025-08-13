# COMO COLETAR DADOS 

nome = input('Qual o seu nome? ') # o que ele digitar vai ser coletado pela variavel "nome"
print(f'O seu nome é {nome}') # função input sempre vai receber uma string


numero_1 = int(input('Digite um número: ')) # aqui, colocando o int antes do input ele está fazendo a coerção
numero_2 = int(input('Digite outro número: ')) 
print(f'A soma dos números é: {numero_1 + numero_2}') # se n"ao fizer a coerção, o resultado não é soma, é concatenação

# Lembrando que esta regra na coerção não é adequada
# na hora da digitação no input, se for digitado uma str apresenta erro e acaba a execução
# como solução, criar uma variavel para os numeros conforme codigo abaixo...

numero_3 = input('Digite um número: ')
numero_4 = input('Digte outro número: ')

int_numero_3 = int(numero_3)
int_numero_4 = int(numero_4)


print(f'A soma dos números é: {int_numero_3 + int_numero_4}')