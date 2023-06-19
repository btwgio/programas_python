#Faça um Programa que peça as duas notas de 5 alunos, calcule e armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.

alunos = []
medias = []
media7 = []
aprovados = []

for i in range(1):
    aluno = str(input('Informe o nome do aluno: '))
    alunos.append(aluno)

    nota_1 = float(input('Informe a primeira nota: '))
    while nota_1 < 0 or nota_1 > 10:
        nota_1 = int(input("Número digitado não está dentro dos limites.\nInforme a primeira nota: "))

    nota_2 = float(input('Informe a segunda nota: '))
    while nota_1 < 0 or nota_1 > 10:
        nota_1 = int(input("Número digitado não está dentro dos limites.\nInforme a segunda nota: "))

    media = (nota_1 + nota_2) / 2
    medias.append(media)
    if media >= 7:
        media7.append(aluno)
 
print(f'Número de alunos com média maior ou igual a 7.0: {len(media7)}')
print(f'Os alunos aprovados são: {media7}.')
