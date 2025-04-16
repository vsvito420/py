# Hier ist ein einfacher Python-Code für die Fibonacci-Berechnung:

def fibonacci(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

print(fibonacci(9000000))  # Berechnet die 9 millionste Fibonacci-Zahl 
