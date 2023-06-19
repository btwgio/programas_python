#Faça um Programa que leia 4 notas, mostre as notas e a média na tela

notas = []
for i in range(4):
    nota = int(input('Informe o valor da nota recebida: '))
    notas.append(nota)
soma = 0
contador = 0 
for x in notas:
    soma += x
    contador += 1
print(f'A média é {soma/contador}')
