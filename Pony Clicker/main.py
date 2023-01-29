import tkinter as tk
import math

window = tk.Tk()

window.title('Pony Clicker')
window.geometry('800x600')

window.rowconfigure([0, 1], weight=1, minsize=200)
window.columnconfigure([0, 5], weight=1, minsize=400)

window_icon = tk.PhotoImage(file='Pony Clicker\\mlp_logo.png')
window.iconphoto(True, window_icon)

#################################################################################################################################
#                                                 configurações da janela acima                                                 #
#################################################################################################################################

def bits_image_click(*args):
    bits_label['text'] += hooves

def bits_per_second_from_cider(*args):
    cider_per_second = 1
    bits_label['text'] += cider_per_second

    window.after(1000, bits_per_second_from_cider)

def buy_hooves(*args):
    global hooves
    global hooves_cost
    global hooves_cost_label

    if bits_label['text'] >= hooves_cost:
        bits_label['text'] -= hooves_cost
        hooves += 1
        total_hooves_label['text'] = hooves

        hooves_cost = math.floor(hooves_cost * 1.5)
        hooves_cost_label['text'] = math.floor(hooves_cost_label['text'] * 1.5)

def buy_cider(*args):
    global cider
    global cider_cost
    global cider_cost_label
    global cider_per_second
    global cider_per_second_label

    if bits_label['text'] >= cider_cost:
        bits_label['text'] -= cider_cost
        cider += 1
        total_cider_label['text'] = cider
        cider_per_second += 1
        cider_per_second_label['text'] = cider_per_second

        cider_cost = math.floor(cider_cost * 1.3)
        cider_cost_label['text'] = math.floor(cider_cost_label['text'] * 1.3)

        window.after(1000, bits_per_second_from_cider)

#################################################################################################################################
#                                                         funções acima                                                         #
#################################################################################################################################

bits_image = tk.PhotoImage(file='Pony Clicker\\poneis.png')
bits_image = bits_image.subsample(15, 15)

bits_image_label = tk.Label(image=bits_image)

bits_image_button = tk.Button(image=bits_image)
bits_image_button.grid(row=1, column=5)
bits_image_button.bind('<ButtonRelease-1>', bits_image_click)

#################################################################################################################################
#                                                     botão de pôneis acima                                                     #
#################################################################################################################################

bits = 0

bits_label = tk.Label(text=bits)
bits_label.grid(row=0, column=5)

#################################################################################################################################
#                                                total de bits e seu campo acima                                                #
#################################################################################################################################

stuff_to_buy = tk.Frame(bg='pink', relief=tk.RIDGE, borderwidth=10)
stuff_to_buy.grid(row=0, column=0, sticky='nsw', rowspan=2)

#################################################################################################################################
#                                                     frame dos itens acima                                                     #
#################################################################################################################################

# campo do nome do item
hooves_text = tk.Label(master=stuff_to_buy, text='Casco', bg='pink')
hooves_text.grid(row=0, column=0)

# botão de compra do item
hooves_buy_button = tk.Button(master=stuff_to_buy, text='Comprar', bg='yellow', activebackground='yellow')
hooves_buy_button.grid(row=0, column=1, padx=10, pady=5)
hooves_buy_button.bind('<ButtonRelease-1>', buy_hooves)

hooves_cost = 10

# campo da palavra "custo"
hooves_cost_text = tk.Label(master=stuff_to_buy, text='Custo: ', bg='pink')
hooves_cost_text.grid(row=0, column=2)

# campo do custo do item
hooves_cost_label = tk.Label(master=stuff_to_buy, text=hooves_cost, bg='pink')
hooves_cost_label.grid(row=0, column=3, padx=5)

hooves = 1

# campo do texto do total comprado do item
total_hooves_text = tk.Label(master=stuff_to_buy, text='Total de Cascos: ', bg='pink')
total_hooves_text.grid(row=1, column=0, padx=5)

# campo do total comprado do item
total_hooves_label = tk.Label(master=stuff_to_buy, text=hooves, bg='pink')
total_hooves_label.grid(row=1, column=1)

#################################################################################################################################
#                                               informações do item "Casco" acima                                               #
#################################################################################################################################

# campo do nome do item
cider_text = tk.Label(master=stuff_to_buy, text='Sidra', bg='pink')
cider_text.grid(row=2, column=0)

# botão de compra do item
cider_buy_button = tk.Button(master=stuff_to_buy, text='Comprar', bg='yellow', activebackground='yellow')
cider_buy_button.grid(row=2, column=1, padx=10, pady=5)
cider_buy_button.bind('<ButtonRelease-1>', buy_cider)

cider_cost = 15

# campo da palavra "custo"
cider_cost_text = tk.Label(master=stuff_to_buy, text='Custo: ', bg='pink')
cider_cost_text.grid(row=2, column=2)

# campo do custo do item
cider_cost_label = tk.Label(master=stuff_to_buy, text=cider_cost, bg='pink')
cider_cost_label.grid(row=2, column=3, padx=5)

cider = 0

# campo do texto do total comprado do item
total_cider_text = tk.Label(master=stuff_to_buy, text='Total de Sidra: ', bg='pink')
total_cider_text.grid(row=3, column=0, padx=5)

# campo do total comprado do item
total_cider_label = tk.Label(master=stuff_to_buy, text=cider, bg='pink')
total_cider_label.grid(row=3, column=1)

cider_per_second = 0

# campo do texto de bits por segundo ganhos pelo item
cider_per_second_text = tk.Label(master=stuff_to_buy, text='Bits por segundo: ', bg='pink')
cider_per_second_text.grid(row=4, column=0, padx=5)

# campo da quantidade de bits por segundo ganhos pelo item
cider_per_second_label = tk.Label(master=stuff_to_buy, text=cider_per_second, bg='pink')
cider_per_second_label.grid(row=4, column=1)

#################################################################################################################################
#                                               informações do item "Sidra" acima                                               #
#################################################################################################################################

window.mainloop()
