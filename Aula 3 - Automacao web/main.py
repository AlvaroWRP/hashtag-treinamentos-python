from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pandas as pd

chrome = webdriver.Chrome()

# pega a cotação do dólar
chrome.get('https://www.google.com/')

chrome.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys('cotação do dólar', Keys.ENTER)

dollar_quotation = chrome.find_element(By.XPATH, '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')

# pega a cotação do euro
chrome.get('https://www.google.com/')

chrome.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys('cotação do euro', Keys.ENTER)

euro_quotation = chrome.find_element(By.XPATH, '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')

# pega a cotação do ouro
chrome.get('https://www.melhorcambio.com/ouro-hoje')

gold_quotation = chrome.find_element(By.XPATH, '//*[@id="comercial"]').get_attribute('value')
gold_quotation = gold_quotation.replace(',', '.')

dataframe_path = 'Aula 3 - Automacao web\\Produtos.xlsx'
dataframe_table = pd.read_excel(dataframe_path)

# transforma as cotações antigas para as atuais
dataframe_table.loc[dataframe_table['Moeda'] == 'Dólar', 'Cotação'] = float(dollar_quotation)
dataframe_table.loc[dataframe_table['Moeda'] == 'Euro', 'Cotação'] = float(euro_quotation)
dataframe_table.loc[dataframe_table['Moeda'] == 'Ouro', 'Cotação'] = float(gold_quotation)

# atualiza a tabela com os novos valores
dataframe_table['Preço de Compra'] = dataframe_table['Preço Original'] * dataframe_table['Cotação']
dataframe_table['Preço de Venda'] = dataframe_table['Preço de Compra'] * dataframe_table['Margem']

# cria um novo arquivo com as atualizações
dataframe_table.to_excel('Aula 3 - Automacao web\\Produtos atualizados.xlsx', index=False)
