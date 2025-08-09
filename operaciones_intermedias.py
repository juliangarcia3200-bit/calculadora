def mcd(a, b):
    while b != 0:
        a, b = b, a % b 
    return a

mdc = mcd(48, 18)
print(f"El máximo común divisor de 48 y 18 es: {mdc}")