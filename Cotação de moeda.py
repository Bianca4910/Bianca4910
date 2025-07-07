import requests
import datetime

def consultar_cotacao(moeda_estrangeira):
    """
    Consulta a cotação de uma moeda estrangeira em relação ao BRL usando a AwesomeAPI.

    Args:
        moeda_estrangeira (str): O código da moeda estrangeira (ex: 'USD', 'EUR').

    Returns:
        dict or None: Um dicionário com os dados da cotação se a consulta for bem-sucedida,
                      caso contrário, None.
    """
    # Converte para maiúsculas para evitar erros de case-sensitive na API
    moeda_estrangeira = moeda_estrangeira.upper()
    url = f"https://economia.awesomeapi.com.br/json/last/{moeda_estrangeira}-BRL"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Lança uma exceção para códigos de status HTTP 4xx/5xx

        data = response.json()
        
        # A chave no JSON retornado é "CODIGOMOEDA BRL", por exemplo, "USDBRL"
        chave_cotacao = f"{moeda_estrangeira}BRL"
        
        if chave_cotacao in data:
            return data[chave_cotacao]
        else:
            print(f"Erro: Não foi possível encontrar a cotação para {moeda_estrangeira}-BRL. Verifique o código da moeda.")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Erro ao conectar à API: {e}")
        return None

def main():
    """
    Função principal do programa para obter e exibir a cotação.
    """
    print("--- Consulta de Cotação de Moeda Estrangeira ---")
    moeda_desejada = input("Digite o código da moeda desejada (ex: USD, EUR, GBP): ").strip()

    cotacao = consultar_cotacao(moeda_desejada)

    if cotacao:
        valor_atual = float(cotacao['bid'])
        valor_maximo = float(cotacao['high'])
        valor_minimo = float(cotacao['low'])
        timestamp = int(cotacao['timestamp'])
        
        # Converte o timestamp para um objeto datetime
        data_hora_atualizacao = datetime.datetime.fromtimestamp(timestamp)

        print(f"\n--- Cotação de {moeda_desejada}/BRL ---")
        print(f"Moeda: {cotacao['name']}")
        print(f"Valor Atual (Compra): R$ {valor_atual:.4f}")
        print(f"Valor Máximo (24h): R$ {valor_maximo:.4f}")
        print(f"Valor Mínimo (24h): R$ {valor_minimo:.4f}")
        print(f"Última Atualização: {data_hora_atualizacao.strftime('%d/%m/%Y %H:%M:%S')}")
        print(f"----------------------------------------\n")
    else:
        print("Não foi possível obter a cotação para a moeda informada. Por favor, tente novamente.")

if __name__ == "__main__":
    main()