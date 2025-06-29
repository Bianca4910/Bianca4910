def calcular_consumo(distancia, combustivel):
    """
    Calcula o consumo médio de combustível.

    Args:
        distancia (float): Distância percorrida em km.
        combustivel (float): Combustível gasto em litros.

    Returns:
        float: Consumo médio em km/l, arredondado para duas casas decimais.
    """
    if combustivel <= 0:
        return 0.0  # Evita divisão por zero
    consumo_medio = distancia / combustivel
    return round(consumo_medio, 2)

def main():
    """
    Função principal para executar a calculadora de consumo de combustível.
    """
    # Dados da viagem
    distancia_percorrida = 300  # km
    combustivel_gasto = 25     # litros

    # Calcular o consumo médio
    consumo = calcular_consumo(distancia_percorrida, combustivel_gasto)

    # Exibir os resultados
    print("--- Detalhes da Viagem ---")
    print(f"Distância percorrida: {distancia_percorrida} km")
    print(f"Combustível gasto: {combustivel_gasto} litros")
    print(f"Consumo médio: {consumo} km/l")
    print("--------------------------")

if __name__ == "__main__":
    main()