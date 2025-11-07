import pandas as pd
from flask import Flask, jsonify

app = Flask(__name__)


#contruir as funcionalidades
@app.route('/')
def homepage():
  return 'A API esta no ar'


@app.route('/pegarvendas')
def pegarvendas():
  tabela = pd.read_csv('advertising.csv')
  total_vendas = tabela['Vendas'].sum()
  print(tabela)
  print(total_vendas)
  resposta = {'total_vendas': total_vendas}
  return jsonify(resposta)


#rodar a nossa api
app.run(host='0.0.0.0')


