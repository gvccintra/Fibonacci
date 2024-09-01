def fibonacci_sequence(n):
    # Inicio dos primeiros dois números da sequência
    fib_sequence = [0, 1]
    
    # Calcula a sequência até o maior número menor ou igual a n
    while fib_sequence[-1] < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    
    return fib_sequence

def is_in_fibonacci(n):
    # Calcula a sequência até o número n
    fib_sequence = fibonacci_sequence(n)
    
    # Verifica se n está na sequência de Fibonacci
    if n in fib_sequence:
        return f"O número {n} pertence à sequência de Fibonacci."
    else:
        return f"O número {n} não pertence à sequência de Fibonacci."

34
numero = int(input("Informe um número: "))
print(is_in_fibonacci(numero))