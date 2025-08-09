
def logatimo(base, numero):
    """
    Calcula el logaritmo de un número dado en una base específica.
    
    :param base: La base del logaritmo.
    :param numero: El número al que se le calculará el logaritmo.
    :return: El logaritmo del número en la base especificada.
    """
    if base <= 0 or numero <= 0:
        raise ValueError("La base y el número deben ser mayores que cero.")
    
    from math import log
    return log(numero, base)


def numero_primo(numero):
    """
    Verifica si un número es primo.
    
    :param numero: El número a verificar.
    :return: True si el número es primo, False en caso contrario.
    """
    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True
  
def mcd(a, b):
    while b != 0:
        a, b = b, a % b 
    return a

mdc = mcd(48, 18)
print(f"El máximo común divisor de 48 y 18 es: {mdc}")

#División Entera
import math
a = 10
b = 3

resultado = a // b
print(resultado)

#Minimo común multiplo

a = 12
b = 18

resultado = math.lcm(a, b)
print("Mínimo común múltiplo:", resultado)

def potencia(base, exponente):
    """
    Calcula la potencia de un número dado.
    
    :param base: La base del número.
    :param exponente: El exponente al que se elevará la base.
    :return: El resultado de la base elevada al exponente.
    """
    return base ** exponente
