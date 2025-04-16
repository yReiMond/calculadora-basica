def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

<<<<<<< HEAD
def divisao(a, b):
    if b == 0:
        raise ValueError("Divião por zero!")
    return a / b

def potencia(base, expoente):
    return base ** expoente
=======
def potencia(base, expoente):
    resultado = 1
    for _ in range(expoente):
        resultado *= base
    return resultado
>>>>>>> feature-potencia-loop
