import csv

def main():
    """
    Função principal para ler e exibir dados de um arquivo CSV de pessoas.
    """
    nome_arquivo = 'pessoas.csv'

    # Criar um arquivo CSV de exemplo se ele não existir
    # Isso é útil para testar o script imediatamente
    try:
        with open(nome_arquivo, 'x', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Nome', 'Idade', 'Cidade'])
            writer.writerow(['Ana Silva', 30, 'São Paulo'])
            writer.writerow(['Bruno Costa', 25, 'Rio de Janeiro'])
            writer.writerow(['Carla Souza', 40, 'Belo Horizonte'])
        print(f"Arquivo '{nome_arquivo}' criado com dados de exemplo.")
    except FileExistsError:
        pass # O arquivo já existe, então não precisamos criá-lo novamente

    print(f"\n--- Conteúdo do arquivo '{nome_arquivo}' ---")
    try:
        with open(nome_arquivo, 'r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)

            # Ler o cabeçalho
            header = next(reader, None)
            if header:
                print(f"Cabeçalho: {', '.join(header)}")
            else:
                print("O arquivo CSV está vazio ou não tem cabeçalho.")
                return

            print("\nDados:")
            for row in reader:
                if row: # Garante que a linha não está vazia
                    print(f"  Nome: {row[0]}, Idade: {row[1]}, Cidade: {row[2]}")
                else:
                    print("  Linha vazia encontrada.")

    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    main()