# igual o outro arquivo, porém sem os gráficos e
# fazendo a predição com as colunas "PrecoOriginal" e "Desconto"

import pandas as pd
from sklearn.linear_model import LinearRegression

dataframe = pd.read_excel(r'Ciencia de dados - CDI\Machine Learning\Regressao Linear\dadosVenda.xlsx')

# localiza as linhas sem valor na coluna "Desconto" e atribui valor 0
dataframe.loc[dataframe['Desconto'].isnull(), 'Desconto'] = 0
dataframe.info()
print()

#####################################################################

x = dataframe[['PrecoOriginal', 'Desconto']]  # dados usados na previsão
y = dataframe['VendaQtd']  # dados que serão previstos

# retorna um array numpy 1D contendo os elementos da série
# nesse caso, são os todos valores da coluna "PrecoVenda"
print(x.values)

# remodela o array de valores de 1D para 2D,
# contendo 1 coluna e n linhas que serão automaticamente calculadas pelo numpy
# isso é necessário pois é o jeito que o scikit recebe arrays
print(x.values.reshape(-1, 1), '\n')

# cria o modelo de regressão linear e treina ele com os dados passados
reg = LinearRegression().fit(x, y)

# mostra a pontuação do modelo
print(f'score -> {reg.score(x, y)}')
print(f'coef_ -> {reg.coef_}')
print(f'intercept_ -> {reg.intercept_}\n')

#####################################################################

# valores que serão usados para predição
dict_values = {
    'prices with discount': [17.50, 17.40, 17.30, 17.20, 17.10],
    'PrecoOriginal': [17.50] * 5,
    'Desconto': [0, 0.1, 0.2, 0.3, 0.4]
}
dict_values = pd.DataFrame(dict_values)

# faz a previsão e retorna uma lista com as quantidades de
# vendas previstas de acordo com os preços escolhidos
prediction = reg.predict(dict_values[['PrecoOriginal', 'Desconto']])

for index, value in enumerate(prediction):
    print(
        # convertendo prices pra uma array pra conseguir loopar sobre ela
        # ao utilizar o [index], será retornado uma lista com um único valor
        # e só pra não ficar uma lista no print, peguei o índice zero
        f'Se o preço do produto for de R${dict_values.values[index][0]:.2f}, '
        f'a previsão é de que ele venda {int(value)} unidades.'
    )

print()

#####################################################################

# checar a quantidade de vendas quando o produto tinha tal preço
# pra comparar com o modelo e ver se a predição foi boa
print(dataframe[dataframe['PrecoVenda'] == 17.10], '\n')

# checagem mais abrangente
print(dataframe[
                (dataframe['PrecoOriginal'] >= 17)
                & (dataframe['PrecoOriginal'] <= 18)
                & (dataframe['Desconto'] >= 0)
                & (dataframe['Desconto'] <= 0.4)
])

# moral da história: usar a coluna "PrecoOriginal" é bem melhor
