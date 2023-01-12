import pandas as pd
import plotly.express as px

database_path = 'C:\\Users\\alvar\\Downloads\\telecom_users.csv'

database_table = pd.read_csv(database_path)

# remoção da coluna com dados não úteis para a análise
database_table = database_table.drop('Unnamed: 0', axis=1)

# transforma a coluna para o tipo de dado correto
database_table['TotalGasto'] = pd.to_numeric(database_table['TotalGasto'], errors='coerce')

# remove as colunas que possuem todos os valores vazios
# devido a uma das colunas ser completamente vazia, ela deve ser removida primeiro para não limpar a base de dados completa
database_table = database_table.dropna(axis=1, how='all')

# remove as linhas que possuem todos os valores vazios
database_table = database_table.dropna(axis=0, how='any')

database_table.info()
print()

# mostrar quantidades de "Sim" e "Não" na coluna "Churn", e em seguida em porcentagem
print(database_table.value_counts(['Churn']), '\n')
print(database_table.value_counts(['Churn'], normalize=True).map('{:.2%}'.format))

# cria um gráfico para cada coluna, com exceção da "IDCliente", que não é útil no caso
for column in database_table:
    if column != 'IDCliente':
        chart = px.histogram(database_table, x=column, color='Churn', text_auto=True, color_discrete_sequence=['blue', 'red'])
        chart.show()

# CONCLUSÕES OBTIDAS COM OS GRÁFICOS:
#
# Os primeiros meses são os que contêm mais cancelamentos:
#     Ideia: uso de promoções e incentivos para segurar o cliente por mais tempo
#     Ideia: melhor gerenciamento da equipe de marketing
#
# Famílias maiores tem uma chance menor de cancelarem do que de famílias menores ou pessoas individuais:
#     Ideia: vender camisinhas furadas
#
# Possível problema na fibra ótica
#
# Quanto mais serviços o cliente possui, menor a chance dele cancelar:
#     Ideia: fazer promoções e afins para fazer o cliente obter esses serviços
#
# Clientes com contrato mensal têm uma chance muito maior de cancelarem:
#     Ideia: reduções de preço e bônus no plano anual
#
# Clientes que pagam por boleto têm uma chance muito maior de cancelarem:
#     Ideia: fazer algo para incentivar a troca do tipo de pagamento
