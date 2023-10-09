import matplotlib.pyplot as plt
import numpy as np

vendas_em_cada_mes = [1500, 1727, 1350, 999, 1050, 1027, 1022, 1500, 2000, 2362, 2100, 2762]
meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']

plt.plot(meses, vendas_em_cada_mes)
plt.xlabel('Meses')
plt.ylabel('Vendas')
plt.axis([0, 12, 0, max(vendas_em_cada_mes) + (max(vendas_em_cada_mes) * 0.1)])
plt.show()

numero_vendas = np.random.randint(1, 5001, 50)
numero_meses = np.arange(1, 51)

plt.plot(numero_meses, numero_vendas, 'm--')
plt.axis([0, 50, 0, max(numero_vendas) + (max(numero_vendas) * 0.1)])
plt.show()

plt.scatter(numero_meses, numero_vendas)
plt.show()

plt.bar(numero_meses, numero_vendas)
plt.show()

plt.figure(figsize=(15, 5))
plt.subplot(1, 3, 1)
plt.plot(numero_meses, numero_vendas, 'm--')
plt.subplot(1, 3, 2)
plt.scatter(numero_meses, numero_vendas)
plt.subplot(1, 3, 3)
plt.bar(numero_meses, numero_vendas)
plt.show()
