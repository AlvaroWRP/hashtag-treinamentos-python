import pandas as pd

dataframe = pd.read_csv(r'Python Impressionador\Analise de Dados\Arquivos CSV\Contoso - Vendas - 2017.csv', sep=';')
print(dataframe, '\n')
print('*' * 50, '\n')

# mostra a coluna escolhida por inteira
print(dataframe['Quantidade Vendida'], '\n')
print('*' * 50, '\n')

# mostra as colunas escolhidas por inteiras, que devem ser passadas dentro de uma lista
print(dataframe[['ID Produto', 'Quantidade Vendida', 'Quantidade Devolvida']], '\n')
print('*' * 50, '\n')

# mostra as linhas escolhidas por inteiras, tendo o mesmo funcionamento de uma lista normal
print(dataframe['Quantidade Vendida'][1:11:2], '\n')
print('*' * 50, '\n')

# também funciona para o dataframe inteiro
print(dataframe[:5], '\n')
print('*' * 50, '\n')

dataframe.info()
