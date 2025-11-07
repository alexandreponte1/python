from random import choice
import string


def senha_segura():
  tamanho_da_senha = 10
  caracteres = string.ascii_letters + string.digits
  # caracteres = string.ascii_letters + string.digits + string.punctuation
  senha_segura = ''
  for i in range(tamanho_da_senha):
    senha_segura += choice(caracteres)
  return senha_segura


senha = senha_segura()


print(senha)