"""
CONSTANTE = "Variáveis" que não vão mudar, convenção usar letras maiusculas.
Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim)
"""


velocidade = 30 # velocidade atual do carro
local_carro = 30 # local em que o carro está na estrada


RADAR_1 = 60 # velocidade máxima do radar 1
LOCAL_1 = 100 # local aonde o radar 1 está
RADAR_RANGE = 1 # A distância aonde o radar pega

velocidade_carro_passou_radar_1 = velocidade > RADAR_1
carro_passou_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and \
   local_carro <= (LOCAL_1 + RADAR_RANGE)

carro_multado_radar_1 = carro_passou_radar_1 and velocidade_carro_passou_radar_1

if velocidade_carro_passou_radar_1:
    print('Velocidade do carro passou do radar 1')

if carro_passou_radar_1:
    print('carro passou radar 1')
else:
    print('não passou no radar')

if  carro_multado_radar_1:
    print('carro multado em radar 1')
else:
    print('dentro da velocidade permitida')