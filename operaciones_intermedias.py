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