# Lógica de programação 
# Passo 0 - Entender o desafio que você quer resolver
# Passo 1 - Percorrer todos os arquivos da pasta base de dados (Pasta Vendas)
import os
import pandas as pd
from IPython.display import display
import plotly.express as px


pathfile = "path dos arquivos"


tabela_total = pd.DataFrame()

lista_arquivo = os.listdir(pathfile)
# print(lista_arquivo)
display(lista_arquivo)
# Passo 2 - Importar as bases de dados de vendas
for arquivo in lista_arquivo:
    if "vendas" in arquivo.lower():
        tabela = pd.read_csv(f"{pathfile}{arquivo}")
        tabela_total = tabela_total.append(tabela)

# Passo 3 - Tratar / Compilar as bases de dados
display(tabela_total)
# Passo 4 - Calcular o produto mais vendido (em quantidade)
tabela_produtos = tabela_total.groupby('Produto').sum()
#Mais de uma coluna ẽ obrigatório dois colchetes
# sort_values ordena os valores
tabela_produtos = tabela_produtos[["Quantidade Vendida", "Preco Unitario"]].sort_values(by="Quantidade Vendida",ascending=False)
display(tabela_produtos)


# Passo 5 - Calcular o produto que mais faturou (em faturamento)
tabela_total['Faturamento'] = tabela_total['Quantidade Vendida'] * tabela_total['Preco Unitario']

tabela_faturamento = tabela_total.groupby('Produto').sum()
tabela_faturamento = tabela_faturamento[["Faturamento"]].sort_values(by="Faturamento", ascending=False)
display(tabela_faturamento)



# Passo 6 - Calcular a loja/cidade que mais vendeu (em faturamento) - criar um gráfico/dashboard
tabela_lojas = tabela_total.groupby('Loja').sum()
tabela_lojas = tabela_lojas[['Faturamento']].sort_values(by="Faturamento", ascending=False)
display(tabela_lojas)


grafico = px.bar(tabela_lojas, x=tabela_lojas.index, y='Faturamento')
grafico.show()
