import pandas as pd
from sklearn.linear_model import LinearRegression
dataframe = pd.read_excel(r'Ciencia de Dados Impressionador\Machine Learning\Regressao Linear\dadosVenda.xlsx')
dataframe.loc[dataframe['Desconto'].isnull(), 'Desconto'] = 0
x = dataframe['PrecoVenda']
y = dataframe['VendaQtd']
x = x.values.reshape(-1, 1)
reg = LinearRegression().fit(x, y)
prices = [17.50, 17.40, 17.30, 17.20, 17.10]
prices = pd.DataFrame(prices)
prediction = reg.predict(prices)
x2 = dataframe[['PrecoOriginal', 'Desconto']]
y2 = dataframe['VendaQtd']
reg2 = LinearRegression().fit(x2, y2)
dict_values = {'prices with discount': [17.50, 17.40, 17.30, 17.20, 17.10], 'PrecoOriginal': [17.50] * 5, 'Desconto': [0, 0.1, 0.2, 0.3, 0.4]}
dict_values = pd.DataFrame(dict_values)
prediction = reg2.predict(dict_values[['PrecoOriginal', 'Desconto']])

# informações dos outros arquivos acima, ignorar

from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_absolute_percentage_error

# cria duas novas colunas para mostrar as previsões de venda de ambos os modelos
dataframe['y_model_1'] = reg.predict(dataframe['PrecoVenda'].values.reshape(-1, 1))
dataframe['y_model_2'] = reg2.predict(dataframe[['PrecoOriginal', 'Desconto']])

print(dataframe.head(), '\n')
print(dataframe.tail(), '\n')

print('Erro do modelo 1: ', end='')
print(mean_absolute_error(dataframe['VendaQtd'], dataframe['y_model_1']))

print('Erro do modelo 2: ', end='')
print(mean_absolute_error(dataframe['VendaQtd'], dataframe['y_model_2']), '\n')

print('Percentual de erro do modelo 1: ', end='')
print(mean_absolute_percentage_error(dataframe['VendaQtd'], dataframe['y_model_1']) * 100)

print('Percentual de erro do modelo 2: ', end='')
print(mean_absolute_percentage_error(dataframe['VendaQtd'], dataframe['y_model_2']) * 100)

# assim, podemos ver que o modelo 2 é muito mais preciso
