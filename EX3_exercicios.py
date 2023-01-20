produtos = ['iphone', 'galaxy', 'ipad', 'tv', 'máquina de café', 'kindle', 'geladeira', 'adega', 'notebook dell', 'notebook hp', 'notebook asus', 'microsoft surface', 'webcam', 'caixa de som', 'microfone', 'câmera canon']
vendas_2019 = [558147, 712350, 573823, 405252, 718654, 531580, 973139, 892292, 422760, 154753, 887061, 438508, 237467, 489705, 328311, 591120]
vendas_2020 = [951642, 244295, 26964, 787604, 867660, 78830, 710331, 646016, 694913, 539704, 324831, 667179, 295633, 725316, 644622, 994303]

for indice, valor in enumerate(vendas_2020):
    if valor > vendas_2019[indice]:
        percentual = vendas_2020[indice] / vendas_2019[indice] - 1

        print(f'O produto "{produtos[indice]}" teve {valor:,} vendas em 2020.\n'
              f'As vendas de 2019 foram de {vendas_2019[indice]:,} unidades.\n'
              f'Isso representa {percentual:.2%} de aumento.\n')

    else:
        percentual = 1 - vendas_2020[indice] / vendas_2019[indice]
        
        print(f'O produto "{produtos[indice]}" teve {valor:,} vendas em 2020.\n'
              f'As vendas de 2019 foram de {vendas_2019[indice]:,} unidades.\n'
              f'Isso representa {percentual:.2%} de queda.\n')

#####################################################################################################################################################
print('#' * 60, '\n')
#####################################################################################################################################################

# mesmo exercício acima, porém feito com tuplas

vendas_produtos = [('iphone', 558147, 951642), ('galaxy', 712350, 244295), ('ipad', 573823, 26964), ('tv', 405252, 787604), ('máquina de café', 718654, 867660), ('kindle', 531580, 78830), ('geladeira', 973139, 710331), ('adega', 892292, 646016), ('notebook dell', 422760, 694913), ('notebook hp', 154753, 539704), ('notebook asus', 887061, 324831), ('microsoft surface', 438508, 667179), ('webcam', 237467, 295633), ('caixa de som', 489705, 725316), ('microfone', 328311, 644622), ('câmera canon', 591120, 994303)]

for nome, vendas_2019, vendas_2020 in vendas_produtos:
    if vendas_2020 > vendas_2019:
        print(f'O produto "{nome}" vendeu mais que ano passado.\n'
              f'Venda em 2019 -> {vendas_2019} | Venda em 2020 -> {vendas_2020}.\n'
              f'Crescimento foi de {vendas_2020 / vendas_2019 - 1:.2%}.\n')
    
    else:
        print(f'O produto "{nome}" vendeu menos que ano passado.\n'
              f'Venda em 2019 -> {vendas_2019} | Venda em 2020 -> {vendas_2020}.\n'
              f'Redução foi de {1 - vendas_2020 / vendas_2019:.2%}.\n')

#####################################################################################################################################################
print('#' * 60, '\n')
#####################################################################################################################################################

estoque = [
    [294, 125, 269, 208, 783, 852, 259, 371, 47, 102, 386, 87, 685, 686, 697, 941, 163, 631, 7, 714, 218, 670, 453],
    [648, 816, 310, 555, 992, 643, 226, 319, 501, 23, 239, 42, 372, 441, 126, 645, 927, 911, 761, 445, 974, 2, 549],
    [832, 683, 784, 449, 977, 705, 198, 937, 729, 327, 339, 10, 975, 310, 95, 689, 137, 795, 211, 538, 933, 751, 522],
    [837, 168, 570, 397, 53, 297, 966, 714, 72, 737, 259, 629, 625, 469, 922, 305, 782, 243, 841, 848, 372, 621, 362],
    [429, 242, 53, 985, 406, 186, 198, 50, 501, 870, 781, 632, 781, 105, 644, 509, 401, 88, 961, 765, 422, 340, 654],
]
fabricas = ['Lira Manufacturing', 'Fábrica Hashtag', 'Python Manufaturas', 'Produções e Cia', 'Manufatura e Cia']
nivel_minimo = 50

for lista in estoque:
    for valor in lista:
        if valor < nivel_minimo:
            fabrica_abaixo_do_nivel_minimo = estoque.index(lista)

            print(fabricas[fabrica_abaixo_do_nivel_minimo], valor)
