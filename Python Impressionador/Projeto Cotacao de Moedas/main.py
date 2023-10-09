# na parte de atualizar cotações múltiplas, somente o último dia selecionado é passado pro Excel. Possível erro na API.

import requests
import numpy as np
import pandas as pd
import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from tkcalendar import DateEntry
from datetime import datetime

# faz a requisição da API
request = requests.get('https://economia.awesomeapi.com.br/json/all')

# transforma o json pra python
coins_info = request.json()

# transforma as chaves (moedas) do dicionário em uma lista que será usada pela ComboBox do tk
coins = list(coins_info.keys())

################################################################################################### API acima

window = tk.Tk()

window.title('Busca de Cotações de Moedas')

window_icon = tk.PhotoImage(file=r'Python Impressionador\Projeto Cotacao de Moedas\coin.png')
window.iconphoto(True, window_icon)

# pega a resolução do monitor
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# define a resolução do aplicativo
window_width = 912
window_height = 684

# define as coordenadas X e Y para centralizar a janela
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2

window.geometry(f'{window_width}x{window_height}+{x}+{y}')
window.resizable(0, 0)  # desativa o redimensionamento da janela

# configura as linhas e colunas para serem ajustadas automaticamente
window.rowconfigure([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], weight=1)
window.columnconfigure([0, 1, 2], weight=1)

################################################################################################### definições da janela acima

def get_quote():
    selected_coin = select_coin_list.get()
    selected_day = single_quote_calendar.get()

    year = selected_day[-4:]
    month = selected_day[3:5]
    day = selected_day[:2]

    link = f'https://economia.awesomeapi.com.br/json/daily/{selected_coin}-BRL/?start_date={year}{month}{day}&end_date={year}{month}{day}'
    request = requests.get(link)

    coin_info = request.json()

    try:
        coin_bid = coin_info[0]['bid']

        coin_bid = float(coin_bid)
        coin_bid = f'{coin_bid:_.4f}'
        coin_bid = coin_bid.replace('.', ',').replace('_', '.')

        single_quote_result['text'] = f'A cotação do {selected_coin} em {selected_day} foi de R${coin_bid}'

    except IndexError:
        single_quote_result['text'] = 'Não houve cotação nesse dia.'

    except KeyError:
        pass


def select_file():
    global file

    file = askopenfilename(title='Selecione um arquivo em Excel (.xlsx)')

    if file:
        if file.endswith('xlsx'):
            selected_file_label['text'] = file

        else:
            selected_file_label['text'] = 'Arquivo no formato inválido'


def update_quotes():
    try:
        df = pd.read_excel(file)

        initial_date = multiple_quote_calendar_initial_date.get()
        initial_date_year = initial_date[-4:]
        initial_date_month = initial_date[3:5]
        initial_date_day = initial_date[:2]

        ending_date = multiple_quote_calendar_ending_date.get()
        ending_date_year = ending_date[-4:]
        ending_date_month = ending_date[3:5]
        ending_date_day = ending_date[:2]

        coins_column = df.iloc[:, 0]

        # itera em cada moeda nas colunas do excel e faz a requisição da API
        for coin in coins_column:
            link = f'https://economia.awesomeapi.com.br/json/daily/{coin}-BRL/?start_date={initial_date_year}{initial_date_month}{initial_date_day}&end_date={ending_date_year}{ending_date_month}{ending_date_day}'

            request = requests.get(link)

            coins_info = request.json()

            # itera as informações de cada moeda
            for info in coins_info:
                bid = float(info['bid'])
                timestamp = int(info['timestamp'])

                date = datetime.fromtimestamp(timestamp)
                date = date.strftime('%d/%m/%Y')

                # caso a coluna com o dia ainda não exista, cria ela e a preenche com NaN
                if date not in df:
                    df[date] = np.nan

                df.loc[coins_column == coin, date] = bid

        df.to_excel(r'Python Impressionador\Projeto Cotacao de Moedas\Moedas atualizado.xlsx')

        updated_file_label['text'] = 'Arquivo atualizado com sucesso.'

    except ValueError:
        pass
    
    except FileNotFoundError:
        pass

################################################################################################### funções acima

single_quote_title = tk.Label(text='Cotação de moeda específica', borderwidth=5, relief='solid')
single_quote_title.grid(row=0, column=0, columnspan=3, sticky='nsew', padx=15, pady=15, ipadx=3, ipady=3)

select_coin_label = tk.Label(text='Selecione a moeda que deseja consultar: ', anchor='e')
select_coin_label.grid(row=1, column=0, columnspan=2, sticky='nsew', padx=15, pady=15)

select_coin_list = ttk.Combobox(values=coins, state='readonly')
select_coin_list.grid(row=1, column=2, sticky='nsew', padx=15, pady=15)

select_day_label = tk.Label(text='Selecione o dia que deseja pegar a cotação: ', anchor='e')
select_day_label.grid(row=2, column=0, columnspan=2, sticky='nsew', padx=15, pady=15)

single_quote_calendar = DateEntry(year=2023, locale='pt_br')
single_quote_calendar.grid(row=2, column=2, sticky='nsew', padx=15, pady=15)

single_quote_result = tk.Label(text='', anchor='e')
single_quote_result.grid(row=3, column=0, columnspan=2, sticky='nsew', padx=15, pady=15)

get_quote_button = tk.Button(text='Pegar cotação', command=get_quote)
get_quote_button.grid(row=3, column=2, sticky='nsew', padx=15, pady=15)

################################################################################################### definições da cotação única acima

multiple_quote_title = tk.Label(text='Cotação de múltiplas moedas', borderwidth=5, relief='solid')
multiple_quote_title.grid(row=4, column=0, columnspan=3, sticky='nsew', padx=15, pady=15, ipadx=3, ipady=3)

select_file_label = tk.Label(text='Selecione um arquivo em Excel (.xlsx) com as moedas na primeira coluna', anchor='e')
select_file_label.grid(row=5, column=0, columnspan=2, sticky='nsew', padx=15, pady=15)

file = ''

select_file_button = tk.Button(text='Escolher arquivo', command=select_file)
select_file_button.grid(row=5, column=2, sticky='nsew', padx=15, pady=15)

selected_file_label = tk.Label(text='Nenhum arquivo selecionado', anchor='e')
selected_file_label.grid(row=6, column=0, columnspan=3, sticky='nsew', padx=15, pady=15)

initial_date_label = tk.Label(text='Cotação das moedas desde: ', anchor='e')
initial_date_label.grid(row=7, column=0, sticky='nsew', padx=15, pady=15)

multiple_quote_calendar_initial_date = DateEntry(year=2023, locale='pt_br', anchor='w')
multiple_quote_calendar_initial_date.grid(row=7, column=1, sticky='nsew', padx=15, pady=15)

ending_date_label = tk.Label(text='Cotação das moedas até: ', anchor='e')
ending_date_label.grid(row=8, column=0, sticky='nsew', padx=15, pady=15)

multiple_quote_calendar_ending_date = DateEntry(year=2023, locale='pt_br', anchor='w')
multiple_quote_calendar_ending_date.grid(row=8, column=1, sticky='nsew', padx=15, pady=15)

update_quotes_button = tk.Button(text='Atualizar cotações', command=update_quotes)
update_quotes_button.grid(row=9, column=0, sticky='nsew', padx=15, pady=15)

updated_file_label = tk.Label(text='', anchor='e')
updated_file_label.grid(row=9, column=1, columnspan=2, sticky='nsew', padx=15, pady=15)

################################################################################################### definições da cotação múltipla acima

close_window_button = tk.Button(text='Encerrar aplicativo', command=lambda: window.quit())
close_window_button.grid(row=10, column=2, sticky='nsew', padx=15, pady=15)

window.mainloop()
