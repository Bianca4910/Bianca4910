def calcular_media(nota1, nota2, nota3):
    """
    Calcula a média de três notas.

    Args:
        nota1 (float): A primeira nota.
        nota2 (float): A segunda nota.
        nota3 (float): A terceira nota.

    Returns:
        float: A média das notas, arredondada para duas casas decimais.
    """
    media = (nota1 + nota2 + nota3) / 3
    return round(media, 2)

def main():
    """
    Função principal para executar a calculadora de média escolar.
    Define as notas, calcula a média e exibe os resultados.
    """
    # Notas do aluno
    nota1 = 7.5
    nota2 = 8.0
    nota3 = 6.5

    # Exibe as notas
    print(f"Nota 1: {nota1}")
    print(f"Nota 2: {nota2}")
    print(f"Nota 3: {nota3}")

    # Calcula a média
    media_final = calcular_media(nota1, nota2, nota3)

    # Exibe o resultado final
    print(f"\nMédia Final: {media_final}")

if __name__ == "__main__":
    main()