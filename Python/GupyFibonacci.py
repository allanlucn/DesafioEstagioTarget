## Criar função para calcular a sequência de Fibonacci.
## Agora a função verifica se o valor de N pertence à sequência.

def sequencia_fib(n):
    a, b = 0, 1
    while a < n:
        a, b = b, a + b
    return a == n

## Criar função para checar se um número x pertence à sequência de Fibonacci.
def pertence_a_sequencia(n):
    return n >= 0 and sequencia_fib(n)

def main():
    while True:
        try:
            numero = int(input("Informe seu número: "))
            if pertence_a_sequencia(numero):
                print(f"{numero} pertence à sequência de Fibonacci.")
            else:
                print(f"{numero} não pertence à sequência de Fibonacci.")
        except ValueError:
            print("O número informado não é válido.")

        # Pede um input para que o usuário possa checar mais um número
        while True:
            loop = input("Deseja continuar? [S/N]: ").strip().upper()
            if loop == "N":
                print("Obrigado por usar o programa!")
                input("Pressione ENTER para sair...")  # Mantém a janela aberta
                return
            elif loop == "S":
                break
            else:
                print("Informe um caractere válido!")

if __name__ == "__main__":
    main()