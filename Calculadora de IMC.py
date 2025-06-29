def calcular_imc(peso, altura):
    """
    Calcula o Índice de Massa Corporal (IMC) com base no peso e altura fornecidos.

    Args:
        peso (float): O peso da pessoa em quilogramas (kg).
        altura (float): A altura da pessoa em metros (m).

    Returns:
        float: O valor do IMC calculado.
    """
    if altura <= 0:
        raise ValueError("A altura não pode ser zero ou negativa.")
    imc = peso / (altura ** 2)
    return imc

def classificar_imc(imc):
    """
    Classifica o IMC de acordo com a tabela padrão.

    Args:
        imc (float): O valor do IMC a ser classificado.

    Returns:
        str: A classificação do IMC (Abaixo do peso, Peso normal, Sobrepeso, Obeso).
    """
    if imc < 18.5:
        return "Abaixo do peso"
    elif imc < 25:
        return "Peso normal"
    elif imc < 30:
        return "Sobrepeso"
    else:
        return "Obeso"

def main():
    """
    Função principal para executar a calculadora de IMC.
    Solicita peso e altura ao usuário, calcula e exibe o IMC e sua classificação.
    """
    print("--- Calculadora de Índice de Massa Corporal (IMC) ---")

    try:
        peso = float(input("Digite seu peso em kg (ex: 70.5): "))
        altura = float(input("Digite sua altura em metros (ex: 1.75): "))

        if peso <= 0:
            print("Erro: O peso não pode ser zero ou negativo. Por favor, tente novamente.")
            return

        imc = calcular_imc(peso, altura)
        classificacao = classificar_imc(imc)

        print(f"\nSeu IMC é: {imc:.2f}")
        print(f"Classificação: {classificacao}")

    except ValueError:
        print("Erro: Entrada inválida. Por favor, digite valores numéricos para peso e altura.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

if __name__ == "__main__":
    main()