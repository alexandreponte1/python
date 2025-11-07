vendedor = "Alexandre"

vendas = 1000

meta = 500

if vendas >= meta:
  print("Bateu a meta")
else:
  print("Não bateu a meta")



class Vendedor():
  def __init__(self, nome):
    self.nome = nome
    self.vendas = 0

  def vendeu(self, vendas):
    self.vendas = vendas

  def bateu_meta(self, meta):
    if self.vendas > meta:
      print(self.nome, "Bateu a meta")
    else:
      print(self.nome, "Não bateu a meta")



vendedor1 = Vendedor("Alexandre")

print(vendedor1.nome)