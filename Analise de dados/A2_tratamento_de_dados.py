import pandas as pd

clients_dataframe = pd.read_csv(r'Analise de Dados\Arquivos CSV\Contoso - Clientes.csv', sep=';', encoding='iso-8859-1')
products_dataframe = pd.read_csv(r'Analise de Dados\Arquivos CSV\Contoso - Cadastro Produtos.csv', sep=';', encoding='iso-8859-1')
stores_dataframe = pd.read_csv(r'Analise de Dados\Arquivos CSV\Contoso - Lojas.csv', sep=';', encoding='iso-8859-1')
sales_dataframe = pd.read_csv(r'Analise de Dados\Arquivos CSV\Contoso - Vendas - 2017.csv', sep=';', encoding='iso-8859-1')

print(clients_dataframe, '\n')
print(products_dataframe, '\n')
print(stores_dataframe, '\n')
print(sales_dataframe, '\n')

# remove as informações não necessárias do dataframe
# eixo 0 = linha | eixo 1 = coluna
clients_dataframe = clients_dataframe.drop(['Unnamed: 7', 'Unnamed: 8', 'Unnamed: 9', 'Unnamed: 10'], axis=1)
print(clients_dataframe, '\n')

clients_dataframe = clients_dataframe[['ID Cliente', 'E-mail']]
print(clients_dataframe, '\n')

products_dataframe = products_dataframe[['ID Produto', 'Nome do Produto']]
print(products_dataframe, '\n')

stores_dataframe = stores_dataframe[['ID Loja', 'Nome da Loja']]
print(stores_dataframe, '\n')

# junta o dataframe escolhido com outro de acordo com uma coluna referência
sales_dataframe = sales_dataframe.merge(clients_dataframe, on='ID Cliente')
sales_dataframe = sales_dataframe.merge(products_dataframe, on='ID Produto')
sales_dataframe = sales_dataframe.merge(stores_dataframe, on='ID Loja')
print(sales_dataframe)

# renomeia uma coluna passando um dicionário, sendo a chave o nome antigo e o valor o nome novo
sales_dataframe = sales_dataframe.rename(columns={'E-mail': 'E-mail Cliente'})
print(sales_dataframe)
