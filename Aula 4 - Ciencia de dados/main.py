# Primeiro deve-se entender o desafio e a área que será aplicada essa inteligência artificial.
# Como é uma previsão de vendas, não há muitos problemas se ela for um pouco menos precisa.
# Isso seria diferente no caso de algo com vidas envolvidas, como remédios ou algo perigoso.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score

dataframe_path = 'Aula 4 - Ciencia de dados\\advertising.csv'

# uma coisa é entender a tabela, pois os valores de venda são menores que os de investimento.
# nesse caso, o investimento está em milhares e as vendas em milhões.
dataframe_table = pd.read_csv(dataframe_path)

# os dados da tabela deveriam ser tratados antes de continuar o processo,
# porém nesse caso não há nenhuma inconsistência nela
dataframe_table.info()
print()

# montar e mostrar o gráfico das informações de acordo com as correlações
sb.heatmap(dataframe_table.corr(), cmap='Blues', annot=True)
plt.show()

# fazer a separação de x e y
###################################
# (       x       )       (  y  ) #
# TV  Radio  Jornal       Vendas  #
# ...  ...    ...          ...    #
# ...  ...    ...          ...    #
# ...  ...    ...          ...    #
###################################
# x = usado para prever   y = previsão

# x -> é todo o resto usado para fazer as previsões
# y -> é a coluna que queremos prever
x = dataframe_table.drop('Vendas', axis=1)
y = dataframe_table['Vendas']

# fazer outra separação para treino e teste
############################################
# TV  Radio  Jornal       Vendas           #
# ...  ...    ...          ...      treino #
# ...  ...    ...          ...      treino #
# ...  ...    ...          ...      treino #
# ...  ...    ...          ...      teste  #
# ...  ...    ...          ...      teste  #
############################################
# treino e teste geralmente com taxas de 70%-80%/20%-30%

# após essas duas divisões, teremos:
# x de treino, x de teste, y de treino e y de teste
train_x, test_x, train_y, test_y = train_test_split(x, y, test_size=0.25)

# cria as IAs (serão usadas 2 para comparação da melhor)
linear_regression_model = LinearRegression()
random_forest_model = RandomForestRegressor()

# treina elas
linear_regression_model.fit(train_x, train_y)
random_forest_model.fit(train_x, train_y)

# faz os testes
linear_regression_prediction = linear_regression_model.predict(test_x)
random_forest_prediction = random_forest_model.predict(test_x)

# mostra o quão perto as previsões estão dos testes
print(f'Percentual da Regressão Linear -> {r2_score(test_y, linear_regression_prediction):.2%}')
print(f'Percentual da Árvore de Decisão -> {r2_score(test_y, random_forest_prediction):.2%}', '\n')

# cria uma tabela auxiliar para ver as comparações das previsões
aux_dataframe = pd.DataFrame()
aux_dataframe['test_y'] = test_y
aux_dataframe['Linear Regression prediction'] = linear_regression_prediction
aux_dataframe['Random Forest prediction'] = random_forest_prediction

print(aux_dataframe, '\n')

centimeter = 1 / 2.54

# visualização gráfica da tabela auxiliar
plt.figure(figsize=(45 * centimeter, 18 * centimeter))
sb.lineplot(data=aux_dataframe)
plt.show()

# recebe uma nova tabela com os gastos futuros em cada canal de comunicação
new_dataframe = pd.read_csv('Aula 4 - Ciencia de dados\\novos.csv')
print(new_dataframe, '\n')

# faz a previsão das vendas usando os dados da nova tabela
# como a Árvore de Decisão é mais precisa, ela será usada na previsão
prediction = random_forest_model.predict(new_dataframe)
print(prediction)
