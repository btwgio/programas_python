#Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. 
#Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual,
#e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . )

mes = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro',
         'Outubro', 'Novembro', 'Dezembro']
temp = []

for i in range(12):
    temperatura = int(input(f'Informe a temperatura do mês {mes[i]} (em Celsius): '))
    temp.append(temperatura)

media = sum(temp) / len(temp)

print(f'A média anual das temperaturas foi {media :.2f} graus Celsius.')
print(f'Esses foram os meses que ultrapassaram a média:')
for i in range(12):
    if temp[i] > media:
        print(f'{mes[i]} : {temp[i]} graus Celsius')
