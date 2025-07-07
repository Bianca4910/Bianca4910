def verificar_senha_forte(senha):
    """
    Verifica se uma senha atende aos critérios de força:
    - Pelo menos 8 caracteres.
    - Contém pelo menos um número.
    """
    if len(senha) < 8:
        print("A senha deve ter pelo menos 8 caracteres.")
        return False

    if not any(char.isdigit() for char in senha):
        print("A senha deve conter pelo menos um número.")
        return False

    return True

def main():
    """
    Função principal que solicita senhas ao usuário até que uma válida seja inserida ou 'sair' seja digitado.
    """
    while True:
        senha_digitada = input("Digite sua senha (ou 'sair' para finalizar): ")

        if senha_digitada.lower() == 'sair':
            print("Programa encerrado.")
            break

        if verificar_senha_forte(senha_digitada):
            print("Senha forte e válida! Bem-vindo(a).")
            break
        else:
            print("Tente novamente.")

if __name__ == "__main__":
    main()