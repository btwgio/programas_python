#Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.

numeros = []
for i in range(10):
    numero = int(input('Informe um número: '))
    numeros.append(numero)
numeros.reverse()
print(numeros)
#também dá certo usando print(numeros::-1)
