>>> from teste import cria_conta, deposita, saca, extrato
>>> conta = cria_conta(123, "Nico", 55.0, 1000.0)
>>> deposita(conta, 300.0)
>>> extrato(conta)
Saldo 355.0
>>> saca(conta, 100.0)
>>> extrato(conta)
Saldo 255.0

<!-- #chama o metodo dentro da classe conta -->
>>> conta.extrato()
Saldo de 155.5 do titular Alexandre


>>> conta.deposita(1500.0)
>>> conta.extrato()
Saldo de 1555.5 do titular Alexandre


>>> from conta import Conta
>>> conta = Conta(124, "Alexandre", 55.5, 1000.0)



>>> from conta import Conta
>>> conta = Conta(124, "Alexandre", 55.5, 1000.0)
Construindo objeto ... <conta.Conta object at 0x10d878a60>
>>> conta2 = Conta(321, "marco", 100.0, 1000.0)
Construindo objeto ... <conta.Conta object at 0x10da33a00>