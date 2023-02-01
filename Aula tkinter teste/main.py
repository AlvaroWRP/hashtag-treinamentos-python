import webbrowser
import pandas as pd
import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk

################################################################################################### teste
checkbox_window = tk.Tk()
checkbox_window.rowconfigure(0, weight=1)
checkbox_window.columnconfigure([0, 1], weight=1)

def terms_of_use(*args):
    webbrowser.open('https://youtu.be/LBjUh4bYF8w')

terms = tk.Label(text='Termos de Uso', fg='blue', font='sans-serif 10 underline', cursor='hand2')
terms.grid(row=0, column=0)
terms.bind('<Button-1>', terms_of_use)

checkbox_var = tk.IntVar()
checkbox = tk.Checkbutton(text='Você concorda com os Termos de Uso deste programa?', variable=checkbox_var)
checkbox.grid(row=1, column=0)

force_confirm = tk.Label(text='')
force_confirm.grid(row=3, column=0)

def confirm():
    if checkbox_var.get():
        checkbox.grid_remove()
        checkbox_button.grid_remove()
        force_confirm.grid_remove()
        approved_image = Image.open('Aula tkinter teste\\pp_like.png')

        resized_approved_image = approved_image.resize((800, 600))
        
        resized_approved_image = ImageTk.PhotoImage(resized_approved_image)

        image_label = tk.Label(image=resized_approved_image)
        image_label.image = resized_approved_image
        image_label.grid(row=0, column=0)

        checkbox_window.after(2000, lambda: checkbox_window.destroy())

    else:
        force_confirm['text'] = 'Aceite imediatamente'

checkbox_button = tk.Button(text='Confirmar', command=confirm)
checkbox_button.grid(row=2, column=0)

checkbox_window.mainloop()
################################################################################################### teste

# cria a instância da classe
window = tk.Tk()

# muda o título da janela
window.title('Janela')

# ajusta o tamanho inicial da janela
window.geometry('1024x768')

# configura a(s) linha(s) e a(s) coluna(s) para ajustarem automaticamente
window.rowconfigure(0, weight=1)
window.columnconfigure([0, 1], weight=1)

# cria um campo de texto
text_1 = tk.Label(text='Sistema de Busca de Cotações de Moedas', background='black', foreground='white', width=50, height=20)
text_1.grid(row=0, column=0, columnspan=4, sticky='NSEW')

text_2 = tk.Label(text='Selecione a moeda desejada', bg='pink', fg='blue', width=80, height=5)
text_2.grid(row=1, column=0, sticky='NSEW')

# cria um campo de texto com um placeholder
entry = tk.Entry(width=30)
entry.insert(0, 'Digite a moeda desejada')
entry.grid(row=1, column=1)

# função que deleta o placeholder do campo de digitação
def click(*args):
    entry.delete(0, tk.END)

# função que limpa o campo caso algo tenha sido digitado e recoloca o placeholder
def unclick(*args):
    entry.delete(0, tk.END)
    entry.insert(0, 'Digite a moeda desejada')

# vincula as funções no foco e desfoco do campo de digitação, respectivamente
entry.bind('<FocusIn>', click)
entry.bind('<FocusOut>', unclick)

temp_dict = {
    'dólar': 5.10,
    'euro': 5.65,
    'ouro': 310.50,
    'bitcoin': 99_999.99,
}

# cria o campo que irá aparecer a cotação
quotation = tk.Label(text='')
quotation.grid(row=2, column=0)

# função que exibe a cotação da moeda digitada ao clicar no botão
def get_quotation_label():
    selected_coin = entry.get()
    selected_coin = selected_coin.lower().strip()
    coin_quotation = temp_dict.get(selected_coin)

    if coin_quotation:
        coin_quotation = f'{coin_quotation:_.4f}'
        coin_quotation = coin_quotation.replace('.', ',').replace('_', '.')
        quotation['text'] = f'A cotação do {selected_coin} é de R${coin_quotation}.'

    else:
        quotation['text'] = f'Cotação do {selected_coin} não encontrada.'

# cria um botão
label_button = tk.Button(text='Pegar cotação', command=get_quotation_label)
label_button.grid(row=2, column=1)

temp_list = list(temp_dict.keys())

entry_list = ttk.Combobox(window, values=temp_list)
entry_list.grid(row=1, column=2)

# mesma função só que para testar o combobox
def get_quotation_combobox():
    selected_coin = entry_list.get()
    selected_coin = selected_coin.lower().strip()
    coin_quotation = temp_dict.get(selected_coin)

    if coin_quotation:
        coin_quotation = f'{coin_quotation:_.4f}'
        coin_quotation = coin_quotation.replace('.', ',').replace('_', '.')
        quotation['text'] = f'A cotação do {selected_coin} é de R${coin_quotation}.'

    else:
        quotation['text'] = f'Cotação do {selected_coin} não encontrada.'

combobox_button = tk.Button(text='Pegar cotação', command=get_quotation_combobox)
combobox_button.grid(row=2, column=2)

text_3 = tk.Label(text='Caso queira pegar mais de uma cotação, escreva o nome da moeda em cada linha')
text_3.grid(row=3, column=0)

# cria uma caixa de texto
text_box = tk.Text(width=10, height=5)
text_box.grid(row=4, column=0)

quotations = tk.Label(text='')
quotations.grid(row=4, column=1)

# função que exibe as cotações de acordo com os textos da caixa de texto
def get_quotations():
    texts = text_box.get('1.0', tk.END)
    texts_list = texts.split('\n')
    del texts_list[-1]
    aux_list = []

    for coin in texts_list:
        coin = coin.lower().strip()
        coin_quotation = temp_dict.get(coin)

        if coin_quotation:
            coin_quotation = f'{coin_quotation:_.4f}'
            coin_quotation = coin_quotation.replace('.', ',').replace('_', '.')
            aux_list.append(f'A cotação do {coin} é de R${coin_quotation}.')

    quotations['text'] = '\n'.join(aux_list)

text_box_button = tk.Button(text='Pegar cotações', command=get_quotations)
text_box_button.grid(row=5, column=0)

radio_button = tk.StringVar(value=' ')
radio_button_label = tk.Label(text='')
radio_button_label.grid(row=8, column=1, columnspan=3)

def get_radio_button():
    radio_button_value = radio_button.get()
    radio_button_label['text'] = radio_button_value

# cria botões de opção única
radio_button_1 = tk.Radiobutton(text='Primeiro botão', variable=radio_button, value='Botão 1')#, command=get_radio_button)
radio_button_2 = tk.Radiobutton(text='Segundo botão', variable=radio_button, value='Botão 2', command=get_radio_button)
radio_button_3 = tk.Radiobutton(text='Terceiro botão', variable=radio_button, value='Botão 3', command=get_radio_button)
radio_button_1.grid(row=6, column=1)
radio_button_2.grid(row=6, column=2)
radio_button_3.grid(row=6, column=3)

radio_button_button = tk.Button(text='Enviar', command=get_radio_button)
radio_button_button.grid(row=7, column=1, columnspan=3)

# função que pede um arquivo do computador e printa ele
def choose_file():
    file_path = askopenfilename()

    dataframe = pd.read_excel(file_path)

    print(dataframe)

button_choose_file = tk.Button(text='Escolher arquivo', command=choose_file)
button_choose_file.grid(row=8, column=0)

# mantêm a janela aberta
window.mainloop()
