def suma(a, b):
    """Suma dos números."""
    return a + b
print("Suma:", suma(5, 3))

def multiplicacion(a, b):
    """Multiplica dos números."""
    return a * b
print("Multiplicación:", multiplicacion(5, 3))

def resta(a, b):
    """Resta dos números."""
    return a - b
print("Resta:", resta(5, 3))

def division(a, b):
    """Divide dos números."""
    if b == 0:
        return "Error: División por cero"
    return a / b
print("División:", division(5, 0))



