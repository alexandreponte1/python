"""
Higher Order Functions
Funcoes de primeira classe
"""


def saudacao(msg, nome):
    return F"{msg}, {nome}!"

def executa(funcao, *args):
    return funcao(*args)

v = executa(saudacao, "Bom dia ", "Alex")

print(
    executa(saudacao, "Bom dia ", "Alex")
)

print(
    executa(saudacao, "Bom noite ", "Maria")
)
