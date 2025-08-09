import math

def potencia(base, exponente):
    """
    Calcula la potencia de un número dado.
    
    :param base: La base de la potencia.
    :param exponente: El exponente al que se elevará la base.
    :return: El resultado de base elevado a exponente.
    """
    return base ** exponente

def raiz_cuadrada(numero):
    """
    Calcula la raíz cuadrada de un número dado.
    
    :param numero: El número del cual se calculará la raíz cuadrada.
    :return: La raíz cuadrada del número.
    """
    if numero < 0:
        return "Error: No se puede calcular la raíz cuadrada de un número negativo"
    return numero ** 0.5
