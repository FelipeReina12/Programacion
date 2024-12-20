def sumar(a, b):
    """Suma dos números."""
    return a + b

def sumar_varios(*args):
    """Suma varios números."""
    return sum(args)

# Ejemplo de uso
resultado_suma_dos = sumar(5, 3)
print(f"Suma de dos números: {resultado_suma_dos}")  # Imprimirá 8

resultado_suma_varios = sumar_varios(1, 2, 3, 4)
print(f"Suma de varios números: {resultado_suma_varios}")  # Imprimirá 10def sumar(a, b):
    """Suma dos números."""
    return a + b

def sumar_varios(*args):
    """Suma varios números."""
    return sum(args)
def sumar(a, b):
    """Suma dos números."""
    return a + b

def sumar_varios(*args):
    """Suma varios números."""
    return sum(args)

def restar(a, b):
    """Resta dos números."""
    return a - b

def restar_varios(*args):
    """Resta varios números, comenzando desde el primer número."""
    resultado = args[0]
    for num in args[1:]:
        resultado -= num
    return resultado

# Ejemplo de uso
resultado_suma_dos = sumar(5, 3)
print(f"Suma de dos números: {resultado_suma_dos}")  # Imprimirá 8

resultado_suma_varios = sumar_varios(1, 2, 3, 4)
print(f"Suma de varios números: {resultado_suma_varios}")  # Imprimirá 10

resultado_resta_dos = restar(5, 3)
print(f"Resta de dos números: {resultado_resta_dos}")  # Imprimirá 2

resultado_resta_varios = restar_varios(10, 2, 3)
print(f"Resta de varios números: {resultado_resta_varios}")  # Imprimirá 5def sumar(a, b):
    """Suma dos números."""
    return a + b

def sumar_varios(*args):
    """Suma varios números."""
    return sum(args)

def restar(a, b):
    """Resta dos números."""
    return a - b

def restar_varios(*args):
    """Resta varios números, comenzando desde el primer número."""
    resultado = args[0]
    for num in args[1:]:
        resultado -= num
    return resultado

# Ejemplo de uso
resultado_suma_dos = sumar(5, 3)
print(f"Suma de dos números: {resultado_suma_dos}")  # Imprimirá 8

resultado_suma_varios = sumar_varios(1, 2, 3, 4)
print(f"Suma de varios números: {resultado_suma_varios}")  # Imprimirá 10

resultado_resta_dos = restar(5, 3)
print(f"Resta de dos números: {resultado_resta_dos}")  # Imprimirá 2

resultado_resta_varios = restar_varios(10, 2, 3)
print(f"Resta de varios números: {resultado_resta_varios}")  # Imprimirá 5
# Ejemplo de uso
resultado_suma_dos = sumar(5, 3)
print(f"Suma de dos números: {resultado_suma_dos}")  # Imprimirá 8

resultado_suma_varios = sumar_varios(1, 2, 3, 4)
print(f"Suma de varios números: {resultado_suma_varios}")  # Imprimirá 10