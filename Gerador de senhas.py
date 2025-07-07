import random
import string

def gerar_senha_aleatoria(comprimento):
    """
    Gera uma senha aleatória com o comprimento especificado, incluindo
    letras maiúsculas, minúsculas, números e caracteres especiais.

    Args:
        comprimento (int): O comprimento desejado para a senha.

    Returns:
        str: A senha aleatória gerada.
    """
    # Define todos os caracteres possíveis para a senha
    caracteres = string.ascii_letters + string.digits + string.punctuation

    # Gera a senha aleatória
    senha = ''.join(random.choice(caracteres) for i in range(comprimento))
    return senha

if __name__ == "main":
    while True:
        try:
            # Solicita ao usuário o comprimento da senha
            comprimento_senha = int(input("Informe o comprimento desejado para a senha: "))

            if comprimento_senha <= 0:
                print("O comprimento da senha deve ser um número positivo. Tente novamente.")
            else:
                # Gera e exibe a senha
                senha_gerada = gerar_senha_aleatoria(comprimento_senha)
                print(f"Sua senha aleatória gerada é: {senha_gerada}")
                break # Sai do loop se a entrada for válida
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro para o comprimento da senha.")