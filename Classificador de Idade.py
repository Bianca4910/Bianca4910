def classificar_idade(idade):
    """
    Classifica a idade em uma das seguintes categorias:
    Criança (0-12), Adolescente (13-17), Adulto (18-59) ou Idoso (60+).

    Args:
        idade (int): A idade a ser classificada.

    Returns:
        str: A categoria da idade.
    """
    if 0 <= idade <= 12:
        return "Criança"
    elif 13 <= idade <= 17:
        return "Adolescente"
    elif 18 <= idade <= 59:
        return "Adulto"
    elif idade >= 60:
        return "Idoso"
    else:
        return "Idade inválida. Por favor, insira um número positivo."

def main():
    """
    Função principal que solicita a idade do usuário e exibe a classificação.
    """
    print("--- Classificador de Idade ---")
    while True:
        try:
            idade_str = input("Por favor, digite sua idade: ")
            idade = int(idade_str)
            
            if idade < 0:
                print("A idade não pode ser negativa. Por favor, insira um valor válido.")
                continue

            categoria = classificar_idade(idade)
            print(f"Você se encaixa na categoria: {categoria}")
            break # Sai do loop se a idade for válida
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro para a idade.")
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")

if __name__ == "__main__":
    main()