def main():
    """
    Função principal do programa para determinar se os números são pares ou ímpares.
    """
    total_pares = 0
    total_impares = 0

    print("Bem-vindo ao verificador de números pares/ímpares!")
    print("Digite um número inteiro por vez. Digite 'fim' para encerrar.")

    while True:
        entrada = input("Digite um número inteiro ou 'fim': ").strip().lower()

        if entrada == 'fim':
            break
        
        try:
            numero = int(entrada)
            if numero % 2 == 0:
                print(f"O número {numero} é PAR.")
                total_pares += 1
            else:
                print(f"O número {numero} é ÍMPAR.")
                total_impares += 1
        except ValueError:
            print(f"Erro: '{entrada}' não é um número inteiro válido. Por favor, tente novamente.")
    
    print("\n--- Resumo ---")
    print(f"Números pares inseridos: {total_pares}")
    print(f"Números ímpares inseridos: {total_impares}")
    print("Obrigado por usar o programa!")

if __name__ == "__main__":
    main()