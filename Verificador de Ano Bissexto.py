def is_leap_year(year):
    """
    Verifica se um ano é bissexto.

    Args:
        year (int): O ano a ser verificado.

    Returns:
        bool: True se o ano for bissexto, False caso contrário.
    """
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

def main():
    """
    Função principal para solicitar o ano ao usuário e exibir o resultado.
    """
    try:
        year = int(input("Digite um ano para verificar se é bissexto: "))
        if is_leap_year(year):
            print(f"O ano {year} é bissexto.")
        else:
            print(f"O ano {year} não é bissexto.")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro para o ano.")

if __name__ == "__main__":
    main()