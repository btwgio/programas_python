#Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos do vetor.

numeros = []
for i in range(10):
    numero = int(input('Informe um número: '))
    numeros.append(numero)

soma = 0 
for numero in numeros:
    soma += numero ** 2

print(f'A soma dos quadrados da lista é {soma}')
print(f'Os números são: {numeros}.')
