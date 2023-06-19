#Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.
numeros = []
adicao = 0
mult = 1

for i in range(5):
    numero = int(input('Informe um número: '))
    numeros.append(numero)

for numero in numeros:
    adicao += numero

for numero in numeros:
    mult *= numero 

print(f'A soma dos números é: {adicao}.')
print(f'A multriplicação entre os números da lista é {mult}.')