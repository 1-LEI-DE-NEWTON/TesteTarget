
def gerar_fibonacci(limite):
    sequencia = [0, 1]
    while sequencia[-1] < limite:
        sequencia.append(sequencia[-1] + sequencia[-2])
    return sequencia

def verificar_fibonacci(numero):
    sequencia = gerar_fibonacci(numero)
    return numero in sequencia

def main():
    numero = int(input("Informe um número: "))
    if verificar_fibonacci(numero):
        print(f"O número {numero} pertence à sequência de Fibonacci.")
    else:
        print(f"O número {numero} não pertence à sequência de Fibonacci.")

if __name__ == "__main__":
    main()