import pandas as pd
import win32com.client as win32

excel_table_path = r'Mini curso\Vendas.xlsx'
excel_table = pd.read_excel(excel_table_path)

# ajuda na visualização caso a tabela tenha muitas colunas
# pd.set_option('display.max_columns', 10)
# print(excel_table)

# calcula o faturamento total para cada loja
total_income_for_each_store = excel_table[['ID Loja', 'Valor Final']].groupby('ID Loja').sum()

print(total_income_for_each_store, '\n')

# calcular a quantidade total de produtos vendidos para cada loja
total_quantity_sold_for_each_store = excel_table[['ID Loja', 'Quantidade']].groupby('ID Loja').sum()

print(total_quantity_sold_for_each_store, '\n')

# calcula o ticket médio por produto em cada loja
ticket = (total_income_for_each_store['Valor Final'] / total_quantity_sold_for_each_store['Quantidade']).to_frame()
ticket = ticket.rename(columns={0: 'Ticket Médio'})

print(ticket)

# envia o e-mail com o relatório
outlook = win32.Dispatch('outlook.application')

mail = outlook.CreateItem(0)
mail.To = 'alvarowroblewski@gmail.com'
mail.Subject = 'Relatório de Vendas'
mail.HTMLBody = f'''<p>Bom dia,</p>

<p>Segue abaixo o relatório das vendas de cada loja.</p>

<p>Faturamentos:</p>
{total_income_for_each_store.to_html(formatters={'Valor Final': 'R${:,.2f}'.format})}

<p>Quantidades vendidas:</p>
{total_quantity_sold_for_each_store.to_html()}

<p>Ticket médio dos produtos:</p>
{ticket.to_html(formatters={'Ticket Médio': 'R${:,.2f}'.format})}

<p>Att.</p>
'''

mail.Send()
