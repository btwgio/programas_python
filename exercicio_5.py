#Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.
caracteres = []
vogais = ['a', 'e', 'i', 'o', 'u']
comparador = ''

for i in range(10):
    caracter = str(input('Informe um caractere: ')).lower()
    if len(caracter) != 1:
        exit('Apenas um caractere!')
    comparador = caracter.isalpha()
    caracteres.append(caracter)

consoantes = []
contador = 0
for caracter in caracteres:
    if caracter not in vogais:
        consoantes.append(caracter)
        contador += 1

print(f'As consoantes são: {consoantes}')
print(f'Temos {contador} consoantes.')