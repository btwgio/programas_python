'''
Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", 
entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".
'''

perguntas = ['Telefonou para vítima?','Esteve no local do crime?', 
            'Mora perto da vítima?', 'Devia para a vítima?', 'Já trabalhou com a vítima?']
negativo = 0
positivo = 0
pos = ['sim', 's', 'ss', 'siim']
neg = ['não', 'nao', 'n', 'nn', 'naoo']

print('Vamos descobrir sua participação no crime de acordo com as suas respostas.')
for i in range(5):
    perg = input(f'{perguntas[i]} Responda com ''sim'' ou não''.\n ').lower()
    if perg in pos:
        positivo += 1
    elif perg in neg:
        negativo += 1
    else:
        exit()

if positivo == 5:
    print('Você é o assassino!')
elif positivo >= 3:
    print('Você é o cúmplice!')
elif positivo == 2:
    print('Você é suspeito!')
else:
    print('Você é inocente!')
    