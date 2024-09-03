#Criar função para checar a existência da letra "a", maiúscula ou minúscula
#além de informar a quantidade de vezes em que ela ocorre.
from logging import exception


def contar_a(n):
    count = n.lower().count('a')
    return count

def main():
    while True:
        try:
            frase= input("Digite uma String: ")
            letra_a = contar_a(frase)

            #caso não haja nenhuma letra A, informar ao usuário
            if letra_a > 0:
                print(f"A letra a aparece {letra_a} vezes na string")
            else:
                print(f"A letra 'a' não aparece nenhuma vez na string")

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

        except exception as e:
            print(f"Erro:{e}")



if __name__ == "__main__":
    main()