"""
Volume do cilindro - questão 6 questionário 5
"""
import math

def calcula_volume_cilindro(diâmetro=1, altura=1):
    área_base = math.pi*diâmetro*diâmetro/4
    volume = área_base*altura
    return volume
