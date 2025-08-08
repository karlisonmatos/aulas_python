# conversao de tipos, coerção
# type convertion, typecasting, coercion

# tipos imutaveis e primitivos: str, int, float, bool

print(1 + 1)
print('a' + 'b') # sinal de + é concatenação, está nesta ação juntando, no caso acima ele está somando pq são 2 inteiros

print(int('1') + 1) # aqui o int dentro do print fez a conversão do '1' em aspas simples para int, permitindo a concatenação
print(float('1.0') + 1)

print(bool('')) # uma string vazia é considerada False

print(str(11) + 'b') # convertendo o numero inteiro para string (str)