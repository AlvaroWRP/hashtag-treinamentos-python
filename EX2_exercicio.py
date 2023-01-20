vendedores = ['Lira', 'João', 'Diego', 'Alon']
produtos = ['ipad', 'iphone']
vendas = [[100, 200], [300, 500], [50, 1000], [900, 10]]

soma = 0

for lista in vendas:
    for valor in lista:
        if valor == lista[1]:
            soma += valor

print('Soma de vendas de iphone ->', soma, '\n')

vendas_mac = [10, 15, 5, 70]
contador = 0

for lista in vendas:
    indice = vendas_mac[contador]
    lista.append(indice)
    contador += 1

print('Novas vendas adicionadas:', *vendas, sep='\n')
