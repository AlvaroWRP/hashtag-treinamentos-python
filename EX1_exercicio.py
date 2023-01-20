meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
vendas_do_primeiro_semestre = [25000, 29000, 22200, 17750, 15870, 19900]
vendas_do_segundo_semestre = [19850, 20120, 17540, 15555, 49051, 9650]
todas_as_vendas_do_ano = vendas_do_primeiro_semestre + vendas_do_segundo_semestre

maior_venda = max(todas_as_vendas_do_ano)
menor_venda = min(todas_as_vendas_do_ano)

indice_da_maior_venda = todas_as_vendas_do_ano.index(maior_venda)
indice_da_menor_venda = todas_as_vendas_do_ano.index(menor_venda)

indice_do_mes_com_maior_venda = meses[indice_da_maior_venda]
indice_do_mes_com_menor_venda = meses[indice_da_menor_venda]

print(f'Mês com maior venda -> {indice_do_mes_com_maior_venda}, com {maior_venda} vendas.')
print(f'Mês com menor venda -> {indice_do_mes_com_menor_venda}, com {menor_venda} vendas.\n')

total_de_vendas_do_ano = sum(todas_as_vendas_do_ano)
percentual_da_maior_venda = maior_venda / total_de_vendas_do_ano

print(f'Total de vendas no ano -> {total_de_vendas_do_ano:,} | Percentual da maior venda do ano -> {percentual_da_maior_venda:.2%}.\n')

top_3_vendas_do_ano = []

top_3_vendas_do_ano.append(maior_venda)
todas_as_vendas_do_ano.remove(maior_venda)

segunda_maior_venda = max(todas_as_vendas_do_ano)
top_3_vendas_do_ano.append(segunda_maior_venda)
todas_as_vendas_do_ano.remove(segunda_maior_venda)

terceira_maior_venda = max(todas_as_vendas_do_ano)
top_3_vendas_do_ano.append(terceira_maior_venda)

print(f'Primeiro lugar -> {top_3_vendas_do_ano[0]} vendas.')
print(f'Segundo lugar -> {top_3_vendas_do_ano[1]} vendas.')
print(f'Terceiro lugar -> {top_3_vendas_do_ano[2]} vendas.')
