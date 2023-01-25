import tkinter as tk

window = tk.Tk()

window.title('Pony Clicker')
window.geometry('800x600')

window_icon = tk.PhotoImage(file='Pony Clicker\\mlp_logo.png')
window.iconphoto(True, window_icon)

#################################################################################################################################
#                                                 configurações da janela acima                                                 #
#################################################################################################################################

def click(*args):
    ponies_label['text'] += click_power

def click_power_upgrade(*args):
    global click_power
    global click_power_upgrade_cost
    global click_power_upgrade_cost_label

    if ponies_label['text'] >= click_power_upgrade_cost:
        ponies_label['text'] -= click_power_upgrade_cost
        click_power += 1
        click_power_upgrade_cost += 10
        click_power_upgrade_cost_label['text'] += 10
        display_click_power['text'] += 1

#################################################################################################################################
#                                                         funções acima                                                         #
#################################################################################################################################

ponies_image = tk.PhotoImage(file='Pony Clicker\\poneis.png')
ponies_image = ponies_image.subsample(15, 15)

ponies_image_label = tk.Label(image=ponies_image)

ponies_image_button = tk.Button(image=ponies_image)
ponies_image_button.grid(row=1, column=2)

ponies_image_button.bind('<Button 1>', click)

#################################################################################################################################
#                                                     botão de pôneis acima                                                     #
#################################################################################################################################

ponies = 0

ponies_label = tk.Label(text=ponies)
ponies_label.grid(row=0, column=2)

#################################################################################################################################
#                                                   contador das pôneis acima                                                   #
#################################################################################################################################

click_power = 1

click_power_upgrade_button = tk.Button(text='Melhorar poder do clique')
click_power_upgrade_button.grid(row=0, column=0)

click_power_upgrade_button.bind('<Button 1>', click_power_upgrade)

click_power_upgrade_cost = 10

click_power_upgrade_cost_label = tk.Label(text=click_power_upgrade_cost)
click_power_upgrade_cost_label.grid(row=0, column=1)

display_click_power = tk.Label(text=click_power)
display_click_power.grid(row=1, column=0)

window.mainloop()
