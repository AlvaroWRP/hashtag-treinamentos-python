import pyautogui as pag
import pyperclip
import pandas as pd

pag.PAUSE = 1
pag.FAILSAFE = True

drive_link = 'https://drive.google.com/drive/folders/1JLa3vHvF_U4J4wTVkjKy0wn6NrrHAkPK'

pag.press('win')
pag.write('brave')
pag.press('enter')

# pyperclip usado no caso de caracteres especiais
pyperclip.copy(drive_link)
pag.hotkey('ctrl', 'v')
pag.press('enter')

# abrir pasta "aula 1"
pag.sleep(5)
pag.doubleClick(385, 290)

# abrir pasta "Exportar"
pag.sleep(2)
pag.doubleClick()

# fazer download da planilha do excel
pag.sleep(2)
pag.rightClick()
pag.click(575, 770)
pag.sleep(5)
pag.click(790, 505)
pag.sleep(2)
pag.click(1900, 1010)

dataframe_path = 'C:\\Users\\alvar\\Downloads\\Vendas - Dez.xlsx'
dataframe_table = pd.read_excel(dataframe_path)

dataframe_table_total_income = sum(dataframe_table['Valor Final'])
dataframe_table_total_quantity = sum(dataframe_table['Quantidade'])

# abrir o e-mail
pag.hotkey('ctrl', 't')
pyperclip.copy('https://mail.google.com/mail/u/0/#inbox')
pag.hotkey('ctrl', 'v')
pag.press('enter')
pag.sleep(5)

# colocar destinatário
pag.click(85, 200)
pag.write('alvarowroblewski@gmail.com')
pag.press('enter')
pag.press('tab')

# colocar assunto
pyperclip.copy('Relatório de Vendas')
pag.hotkey('ctrl', 'v')
pag.press('tab')

message = f'''Olá,

O faturamento total foi de: R${dataframe_table_total_income:,.2f}
A quantidade de produtos vendidos foi de: {dataframe_table_total_quantity:,}

Att.
'''

# escrever mensagem
pyperclip.copy(message)
pag.hotkey('ctrl', 'v')

# anexar arquivo excel
pag.click(1425, 1005)
pyperclip.copy(dataframe_path)
pag.hotkey('ctrl', 'v')
pag.press('enter')

confirmation = pag.confirm(text='Are you sure? If you click "Confirm", the e-mail will be send.', title='Confirmation box', buttons=['Confirm', 'Cancel'])

if confirmation == 'Confirm':
    pag.click(1300, 1005)
