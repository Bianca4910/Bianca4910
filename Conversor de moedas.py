def main():
    """
    Converte um valor em reais para dólares e euros e exibe os resultados.
    """
    valor_reais = 100.00
    taxa_dolar = 5.20
    taxa_euro = 6.15

    # Calcula os valores convertidos
    valor_dolar = valor_reais / taxa_dolar
    valor_euro = valor_reais / taxa_euro

    # Exibe os resultados arredondados para duas casas decimais
    print(f"R$ {valor_reais:.2f} é equivalente a:")
    print(f"US$ {valor_dolar:.2f}")
    print(f"€ {valor_euro:.2f}")

if __name__ == "__main__":
    main()