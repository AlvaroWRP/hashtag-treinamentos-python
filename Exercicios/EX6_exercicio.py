def converter_em_numero(valor):
    valor = valor.replace('R$ ', '').replace('.', '').replace(',', '.')
    valor = float(valor)

    return valor

def calcular_imposto_mensal(valor):
    iss = 0.05 * valor
    pis = 0.0065 * valor
    cofins = 0.03 * valor
    imposto_mensal = iss + pis + cofins

    return imposto_mensal

def calcular_imposto_trimestral(valor):
    ir = 0.048 * valor
    csll = 0.0288 * valor
    ir_adicional = 0

    if valor > 20000:
        ir_adicional = (valor - 20000) * 0.1

    imposto_trimestral = ir + ir_adicional + csll

    return imposto_trimestral

faturamento = {
    'Jan': 'R$ 95.141,98',
    'Fev': 'R$ 95.425,16',
    'Mar': 'R$ 89.716,31',
    'Abr': 'R$ 78.459,99',
    'Mai': 'R$ 71.087,28',
    'Jun': 'R$ 83.911,06',
    'Jul': 'R$ 56.467,26',
    'Ago': 'R$ 88.513,58',
    'Set': 'R$ 66.552,49',
    'Out': 'R$ 80.164,07',
    'Nov': 'R$ 66.964,33',
    'Dez': 'R$ 71.525,25',
}

for chave, valor in faturamento.items():
    valor = converter_em_numero(valor)

    imposto_mensal = calcular_imposto_mensal(valor)
    imposto_trimestral = calcular_imposto_trimestral(valor)

    valor = (valor, imposto_mensal, imposto_trimestral)

    print(f'{chave} -> {valor}')
