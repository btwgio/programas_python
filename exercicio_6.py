#Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.

numeros = []
impares = []
pares = []

for i in range(20):
    numero = int(input('Informe um número: '))
    numeros.append(numero)
    
    if numero % 2 == 0:
        pares.append(numero)
        
    else:
        impares.append(numero)
    
print(f'Os números informados são: {numeros}.')
print(f'Os números pares são: {pares}.')
print(f'Os números ímpares são: {impares}.')