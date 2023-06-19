#Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem lida.

idade = []
altura = []

for i in range(2):
    idade_1 = int(input('Informe a sua idade: '))
    altura_1 = float(input('Informe a sua altura: '))
    idade.append(idade_1)
    altura.append(altura_1)

print(f'As idades são: {idade[::-1]}')
print(f'As alturas são: {altura[::-1]}')