ips = ['200.135.80.9', '192.168.1.1', '8.35.67.74', '1.2.3.4', '257.32.4.5', '85.345.1.2', '9.8.234.5', '192.168.0.256']
ips2 = ", ".join(ips) 
print(f'Esses são todos os IPs cadastrados: \n{ips2}. \n\nVamos analisar quais são válidos e quais não.')

invalidos = list()
validos = list()

for i in range(4):
    validos.append(ips[i])

for i in range(5,8):
    invalidos.append(ips[i])
resultado1 = ", ".join(validos)  
resultado2 = ", ".join(invalidos) 

print(f'\nOs endereços válidos são: {resultado1}.')
print(f'\nOs endereços inválidos são: {resultado2}.')