import json
import os

def criar_ou_atualizar_dados_pessoa(nome_arquivo, dados_pessoa):
    """
    Cria um novo arquivo JSON com os dados da pessoa ou atualiza um existente.

    Args:
        nome_arquivo (str): O nome do arquivo JSON.
        dados_pessoa (dict): Um dicionário contendo 'Nome', 'Idade' e 'Cidade'.
    """
    try:
        with open(nome_arquivo, 'w', encoding='utf-8') as f:
            json.dump(dados_pessoa, f, ensure_ascii=False, indent=4)
        print(f"Dados salvos com sucesso em '{nome_arquivo}'.")
    except IOError as e:
        print(f"Erro ao escrever no arquivo '{nome_arquivo}': {e}")

def ler_dados_pessoa(nome_arquivo):
    """
    Lê os dados de uma pessoa de um arquivo JSON.

    Args:
        nome_arquivo (str): O nome do arquivo JSON.

    Returns:
        dict or None: Um dicionário com os dados da pessoa se o arquivo existir e for válido,
                      caso contrário, retorna None.
    """
    if not os.path.exists(nome_arquivo):
        print(f"O arquivo '{nome_arquivo}' não foi encontrado.")
        return None
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as f:
            dados = json.load(f)
        print(f"Dados lidos de '{nome_arquivo}':")
        return dados
    except json.JSONDecodeError as e:
        print(f"Erro ao decodificar JSON do arquivo '{nome_arquivo}': {e}")
        return None
    except IOError as e:
        print(f"Erro ao ler o arquivo '{nome_arquivo}': {e}")
        return None

def main():
    """
    Função principal para executar a lógica de leitura e escrita de dados JSON.
    """
    nome_arquivo_json = 'pessoa.json'

    # 1. Definir os dados da pessoa
    minha_pessoa = {
        "Nome": "João Silva",
        "Idade": 30,
        "Cidade": "Curitiba"
    }

    # 2. Escrever os dados no arquivo JSON
    criar_ou_atualizar_dados_pessoa(nome_arquivo_json, minha_pessoa)

    print("\n--- Tentando ler os dados ---")

    # 3. Ler os dados do arquivo JSON
    dados_lidos = ler_dados_pessoa(nome_arquivo_json)

    if dados_lidos:
        print(f"Nome: {dados_lidos.get('Nome')}")
        print(f"Idade: {dados_lidos.get('Idade')}")
        print(f"Cidade: {dados_lidos.get('Cidade')}")
    else:
        print("Não foi possível ler os dados da pessoa.")

if __name__ == "__main__":
    main()