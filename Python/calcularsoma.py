def calcular_soma(indice):
    soma = 0
    k = 1
    while k < indice:
        k += 1
        soma += k
    return soma

def main():
    indice = 12
    resultado = calcular_soma(indice)
    print(f"A soma dos números de 1 até {indice} é: {resultado}")

if __name__ == "__main__":
    main()