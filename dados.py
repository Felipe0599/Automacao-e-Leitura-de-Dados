import pandas as pd

dados = pd.read_excel(r"F:\Automação\Vendas - Dez (1).xlsx")

print(dados)

faturamento = dados["Valor Final"].sum()
quantidade = dados["Quantidade"].sum()

print(faturamento)
print(quantidade)
